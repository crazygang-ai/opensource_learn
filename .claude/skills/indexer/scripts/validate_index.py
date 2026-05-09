#!/usr/bin/env python3
"""Validate root README index and taxonomy against *-learn directories."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


LINK_RE = re.compile(r'<a\s+href="\./([^"]+?-learn)">([^<]+)</a>')
TR_RE = re.compile(r"<tr>(.*?)</tr>", re.S)
TD_RE = re.compile(r"<td(?P<attrs>[^>]*)>(?P<body>.*?)</td>", re.S)
ROWSPAN_RE = re.compile(r'rowspan="(?P<n>\d+)"')
TAG_RE = re.compile(r"<[^>]+>")
TAXONOMY_PATH_RE = re.compile(r"^\s+path:\s*(?P<path>(?:ai|dev-tools)/[A-Za-z0-9._-]+)\s*$", re.M)


@dataclass
class Span:
    kind: str
    label: str
    declared: int
    actual: int = 0


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def learn_dirs(repo_root: Path) -> set[str]:
    dirs: set[str] = set()
    for readme in repo_root.glob("*/*/*/README.md"):
        if not readme.parent.name.endswith("-learn"):
            continue
        if readme.is_file():
            dirs.add(rel(readme.parent, repo_root))
    return dirs


def category_dirs(repo_root: Path) -> set[str]:
    dirs: set[str] = set()
    for domain in ("ai", "dev-tools"):
        domain_dir = repo_root / domain
        if not domain_dir.is_dir():
            continue
        for child in domain_dir.iterdir():
            if child.is_dir() and not child.name.startswith("."):
                dirs.add(rel(child, repo_root))
    return dirs


def taxonomy_paths(repo_root: Path) -> tuple[set[str], list[tuple[str, str]]]:
    taxonomy = repo_root / "taxonomy.yaml"
    if not taxonomy.is_file():
        return set(), [("missing-taxonomy-file", "taxonomy.yaml")]

    text = taxonomy.read_text(encoding="utf-8", errors="ignore")
    paths = {match.group("path").strip("/") for match in TAXONOMY_PATH_RE.finditer(text)}
    if not paths:
        return paths, [("empty-taxonomy-paths", "taxonomy.yaml")]
    return paths, []


def indexed_dirs(readme_text: str) -> set[str]:
    return {match.group(1).strip("/") for match in LINK_RE.finditer(readme_text)}


def clean_cell(body: str) -> str:
    return TAG_RE.sub("", body).strip()


def parse_spans(readme_text: str) -> list[Span]:
    spans: list[Span] = []
    current_domain: Span | None = None
    current_category: Span | None = None

    for row in TR_RE.findall(readme_text):
        if "<th>" in row:
            continue
        if not LINK_RE.search(row):
            continue

        cells = list(TD_RE.finditer(row))
        for cell in cells:
            body = cell.group("body")
            attrs = cell.group("attrs")
            rowspan_match = ROWSPAN_RE.search(attrs)
            if not rowspan_match:
                continue

            label = clean_cell(body)
            declared = int(rowspan_match.group("n"))
            if "<b>" in body:
                current_domain = Span("domain", label, declared)
                spans.append(current_domain)
                current_category = None
            else:
                current_category = Span("category", label, declared)
                spans.append(current_category)

        if current_domain:
            current_domain.actual += 1
        if current_category:
            current_category.actual += 1

    return spans


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("Usage: validate_index.py <repo-root>", file=sys.stderr)
        return 64

    repo_root = Path(argv[0]).expanduser().resolve()
    readme = repo_root / "README.md"
    if not readme.is_file():
        print(f"FAIL\tmissing README.md\t{readme}")
        return 1

    text = readme.read_text(encoding="utf-8", errors="ignore")
    dirs = learn_dirs(repo_root)
    links = indexed_dirs(text)
    categories = category_dirs(repo_root)
    taxonomy, taxonomy_issues = taxonomy_paths(repo_root)

    issues: list[tuple[str, str]] = list(taxonomy_issues)
    for item in sorted(dirs - links):
        issues.append(("unindexed-dir", item))
    for item in sorted(links - dirs):
        issues.append(("stale-link", item))
    for item in sorted(categories - taxonomy):
        issues.append(("missing-taxonomy-category", item))
    for item in sorted(taxonomy - categories):
        issues.append(("stale-taxonomy-path", item))
    for span in parse_spans(text):
        if span.declared != span.actual:
            issues.append(("rowspan", f"{span.kind}:{span.label}: declared={span.declared} actual={span.actual}"))

    if issues:
        print(f"FAIL\t{len(issues)} issue(s)")
        for kind, detail in issues:
            print(f"{kind}\t{detail}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
