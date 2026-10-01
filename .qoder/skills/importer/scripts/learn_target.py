#!/usr/bin/env python3
"""Resolve GitHub repository identity, check existing notes, and fetch the target repository README."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse, urlsplit


GITHUB_RE = re.compile(r"github\.com[:/](?P<owner>[^/\s\]'<>\")]+)/(?P<repo>[^/\s#?\]'<>\")]+)", re.I)

API_HOST = "api.github.com"
RAW_HOST = "raw.githubusercontent.com"
ALLOWED_HOSTS = (API_HOST, RAW_HOST)
RAW_README_VARIANTS = ("README.md", "readme.md", "README.markdown", "README.rst", "docs/README.md")
REQUEST_TIMEOUT = 6.0
MIN_README_BYTES = 40
USER_AGENT = "opensource-learn-importer"

EXIT_INPUT = 2       # URL 非法，或仓库不存在 / 不可访问（可能为私有）
EXIT_NETWORK = 3     # 两级取 README 均失败
EXIT_NO_README = 4   # 仓库存在但无 README，stderr 的 META 行给出分类 metadata
EXIT_JUNK = 5        # 取回内容疑似错误页


def normalize_repo_name(repo: str) -> str:
    repo = repo.rstrip(").,]\"'<>")
    if repo.endswith(".git"):
        repo = repo[:-4]
    return repo.strip("/")


def parse_github_url(url: str) -> tuple[str, str, str, str, str]:
    raw = url.strip()
    match = GITHUB_RE.search(raw)
    if not match:
        parsed = urlparse(raw)
        parts = [p for p in parsed.path.split("/") if p]
        if parsed.netloc.lower() != "github.com" or len(parts) < 2:
            raise ValueError(f"unsupported GitHub URL: {url}")
        owner, repo = parts[0], parts[1]
    else:
        owner, repo = match.group("owner"), match.group("repo")

    repo = normalize_repo_name(repo)
    owner = owner.strip()
    if not owner or not repo:
        raise ValueError(f"unsupported GitHub URL: {url}")

    canonical = f"https://github.com/{owner}/{repo}"
    learn_dir = f"{owner}-{repo}-learn"
    clone_url = f"{canonical}.git"
    return owner, repo, learn_dir, canonical, clone_url


def normalize_owner_repo(owner: str, repo: str) -> str:
    return f"{owner.lower()}/{normalize_repo_name(repo).lower()}"


def extract_github_refs(text: str) -> set[str]:
    refs: set[str] = set()
    for match in GITHUB_RE.finditer(text):
        owner = match.group("owner")
        repo = normalize_repo_name(match.group("repo"))
        refs.add(normalize_owner_repo(owner, repo))
    return refs


def iter_learn_readmes(repo_root: Path):
    for readme in repo_root.glob("*/*/*/README.md"):
        if not readme.parent.name.endswith("-learn"):
            continue
        if readme.is_file():
            yield readme


def cmd_parse(args: argparse.Namespace) -> int:
    owner, repo, learn_dir, canonical, clone_url = parse_github_url(args.github_url)
    print(f"OWNER\t{owner}")
    print(f"REPO\t{repo}")
    print(f"LEARN_DIR\t{learn_dir}")
    print(f"GITHUB_URL\t{canonical}")
    print(f"CLONE_URL\t{clone_url}")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).expanduser().resolve()
    owner, repo, learn_dir, canonical, _ = parse_github_url(args.github_url)
    target = normalize_owner_repo(owner, repo)
    exact_dir = learn_dir.lower()

    for readme in iter_learn_readmes(repo_root):
        learn_path = readme.parent
        try:
            text = readme.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if target in extract_github_refs(text):
            print(f"EXISTS\t{learn_path}\trepository-url\t{canonical}")
            return 0
        if learn_path.name.lower() == exact_dir:
            print(f"EXISTS\t{learn_path}\tdirectory-name\t{canonical}")
            return 0

    print(f"NOT_EXISTS\t{learn_dir}\t{canonical}")
    return 0


def resolve_token() -> tuple[str | None, str]:
    for name in ("GH_TOKEN", "GITHUB_TOKEN"):
        value = os.environ.get(name, "").strip()
        if value:
            return value, f"env:{name}"
    return None, "anonymous"


def backoff_delay(attempt: int, base: float) -> float:
    return base * (2 ** min(attempt, 3))


def retry_after_seconds(headers) -> float | None:
    if headers is None:
        return None
    raw = headers.get("Retry-After")
    if raw is None:
        return None
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def remaining_zero(headers) -> bool:
    if headers is None:
        return False
    remaining = headers.get("x-ratelimit-remaining")
    return remaining is not None and str(remaining).strip() == "0"


def http_get(
    url: str,
    *,
    token: str | None,
    attempts: int,
    sleep: float,
    accept: str,
) -> tuple[int | None, object, bytes, str, str | None]:
    """GET with script-controlled backoff：传输错误与 5xx/408/429 重试，其余 4xx 立即返回。"""
    err: str | None = None
    attempts = max(attempts, 1)
    for attempt in range(attempts):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
        if token and urlsplit(url).hostname == API_HOST:
            # add_unredirected_header：30x 跳到其他 host 时凭据不会被复制到新请求
            req.add_unredirected_header("Authorization", "Bearer " + token)
        try:
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                body = resp.read()
                final_url = resp.geturl()
                if urlsplit(final_url).hostname not in ALLOWED_HOSTS:
                    return None, resp.headers, b"", final_url, f"unexpected final host {urlsplit(final_url).hostname}"
                return resp.status, resp.headers, body, final_url, None
        except urllib.error.HTTPError as exc:
            if exc.code == 429:
                wait = retry_after_seconds(exc.headers)
                if wait is not None and wait <= 5:
                    err = f"HTTP 429 Retry-After={wait}s"
                    time.sleep(wait)
                    continue
                return exc.code, exc.headers, exc.read() or b"", url, f"HTTP 429 Retry-After={wait}s"
            if exc.code >= 500 or exc.code == 408:
                err = f"HTTP {exc.code}"
            else:
                return exc.code, exc.headers, exc.read() or b"", url, None
        except (urllib.error.URLError, OSError) as exc:
            err = f"{type(exc).__name__}: {exc}"
        if attempt + 1 < attempts:
            time.sleep(backoff_delay(attempt, sleep))
    return None, None, b"", url, err


def junk_reason(body: bytes, headers) -> str | None:
    if headers is not None:
        content_type = str(headers.get("content-type") or "")
        if "text/html" in content_type.lower():
            return f"content-type {content_type.strip()}"
    if len(body) < MIN_README_BYTES:
        return f"body only {len(body)} bytes"
    head = body.lstrip()[:64]
    if re.match(rb"(?i)<!doctype\s+html", head) or re.match(rb"(?i)<html[\s>]", head):
        return "body looks like an HTML document"
    return None


def extract_meta(body: bytes) -> list[str]:
    try:
        data = json.loads(body.decode("utf-8", errors="replace"))
    except ValueError:
        data = {}
    description = " ".join(str(data.get("description") or "").split())
    topics = ", ".join(str(item) for item in (data.get("topics") or []))
    return [
        f"description\t{description}",
        f"topics\t{topics}",
        f"language\t{data.get('language') or ''}",
        f"default_branch\t{data.get('default_branch') or ''}",
    ]


def planned_urls(owner: str, repo: str) -> list[str]:
    urls = [
        f"https://{API_HOST}/repos/{owner}/{repo}/readme",
        f"https://{API_HOST}/repos/{owner}/{repo}",
    ]
    urls.extend(f"https://{RAW_HOST}/{owner}/{repo}/HEAD/{variant}" for variant in RAW_README_VARIANTS)
    return urls


def cmd_readme(args: argparse.Namespace) -> int:
    owner, repo, _, canonical, _ = parse_github_url(args.github_url)
    token, token_source = resolve_token()
    api_attempts = args.attempts or 3
    raw_attempts = args.attempts or 5

    if args.dry_run:
        print(f"token_source={token_source}", file=sys.stderr)
        for url in planned_urls(owner, repo):
            print(f"URL\t{url}", file=sys.stderr)
        return 0

    state = {"token": token}

    def api_get(url: str, accept: str):
        status, headers, body, final_url, err = http_get(
            url, token=state["token"], attempts=api_attempts, sleep=args.sleep, accept=accept)
        if status == 401 and state["token"] is not None:
            print(f"WARN\tTOKEN_INVALID source={token_source}: {API_HOST} returned 401, retrying anonymously", file=sys.stderr)
            state["token"] = None
            status, headers, body, final_url, err = http_get(
                url, token=None, attempts=api_attempts, sleep=args.sleep, accept=accept)
        return status, headers, body, final_url, err

    reasons: list[str] = []

    if args.tier in ("auto", "api"):
        readme_url = f"https://{API_HOST}/repos/{owner}/{repo}/readme"
        status, headers, body, _, err = api_get(readme_url, "application/vnd.github.raw")
        if status == 200:
            reason = junk_reason(body, headers)
            if reason:
                status, headers, body, _, err = api_get(readme_url, "application/vnd.github.raw")
                if status == 200:
                    reason = junk_reason(body, headers)
            if reason is None:
                sys.stdout.buffer.write(body)
                print(f"STATUS\ttier=api ok token_source={token_source} remaining={headers.get('x-ratelimit-remaining')}", file=sys.stderr)
                return 0
            reasons.append(f"api: content rejected ({reason})")
            if args.tier == "api":
                print(f"ERROR\tREADME content rejected: {reason}", file=sys.stderr)
                return EXIT_JUNK
        elif status in (404, 451):
            repo_url = f"https://{API_HOST}/repos/{owner}/{repo}"
            mstatus, mheaders, mbody, _, merr = api_get(repo_url, "application/vnd.github+json")
            if mstatus == 200:
                for line in extract_meta(mbody):
                    print(f"META\t{line}", file=sys.stderr)
                print(f"STATUS\trepo exists without README (tier=api) token_source={token_source}", file=sys.stderr)
                return EXIT_NO_README
            if mstatus in (404, 451):
                print(f"ERROR\trepository not found or not accessible (may be private): {canonical}", file=sys.stderr)
                return EXIT_INPUT
            reasons.append(f"api: readme HTTP {status}, repo check HTTP {mstatus} ({merr or ''})".rstrip(" ()"))
        elif status == 403 and remaining_zero(headers):
            reasons.append("api: rate limited (remaining=0)")
        elif status is not None:
            reasons.append(f"api: HTTP {status}")
        else:
            reasons.append(f"api: {err or 'request failed'}")

    if args.tier == "api":
        print(f"ERROR\tapi tier failed: {'; '.join(reasons)}", file=sys.stderr)
        return EXIT_NETWORK

    for variant in RAW_README_VARIANTS:
        raw_url = f"https://{RAW_HOST}/{owner}/{repo}/HEAD/{variant}"
        status, headers, body, _, err = http_get(
            raw_url, token=None, attempts=raw_attempts, sleep=args.sleep, accept="text/plain")
        if status == 200:
            reason = junk_reason(body, headers)
            if reason:
                status, headers, body, _, _ = http_get(
                    raw_url, token=None, attempts=1, sleep=args.sleep, accept="text/plain")
                if status == 200:
                    reason = junk_reason(body, headers)
            if reason is None:
                sys.stdout.buffer.write(body)
                print(f"STATUS\ttier=raw variant={variant} ok", file=sys.stderr)
                return 0
            print(f"ERROR\tREADME content rejected: {reason}", file=sys.stderr)
            return EXIT_JUNK
        if status == 404:
            continue
        if status is None:
            reasons.append(f"raw {variant}: {err or 'request failed'}")
        else:
            reasons.append(f"raw {variant}: HTTP {status}")

    detail = "; ".join(reasons) if reasons else f"raw: no README variant matched ({', '.join(RAW_README_VARIANTS)})"
    print(f"ERROR\tfailed to fetch README: {detail}", file=sys.stderr)
    return EXIT_NETWORK


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    parse_parser = subparsers.add_parser("parse")
    parse_parser.add_argument("github_url")
    parse_parser.set_defaults(func=cmd_parse)

    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("repo_root")
    check_parser.add_argument("github_url")
    check_parser.set_defaults(func=cmd_check)

    readme_parser = subparsers.add_parser("readme")
    readme_parser.add_argument("github_url")
    readme_parser.add_argument("--tier", choices=("auto", "api", "raw"), default="auto",
                               help="force a single tier for debugging; default auto")
    readme_parser.add_argument("--attempts", type=int, default=0,
                               help="per-request attempts, overriding tier defaults (api 3 / raw 5)")
    readme_parser.add_argument("--sleep", type=float, default=0.7, help="base backoff delay in seconds")
    readme_parser.add_argument("--dry-run", dest="dry_run", action="store_true",
                               help="print token source and planned URLs, no network")
    readme_parser.set_defaults(func=cmd_readme)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except ValueError as exc:
        print(f"ERROR\t{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
