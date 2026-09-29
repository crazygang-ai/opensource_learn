#!/usr/bin/env python3
"""Resolve GitHub repository identity and check opensource_learn notes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


GITHUB_RE = re.compile(r"github\.com[:/](?P<owner>[^/\s\]'<>\")]+)/(?P<repo>[^/\s#?\]'<>\")]+)", re.I)


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

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except ValueError as exc:
        print(f"ERROR\t{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
