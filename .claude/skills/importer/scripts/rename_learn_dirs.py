#!/usr/bin/env python3
"""Rename existing learning directories to <owner>-<repo>-learn."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


GITHUB_RE = re.compile(r"github\.com[:/](?P<owner>[^/\s\]'<>\")]+)/(?P<repo>[^/\s#?\]'<>\")]+)", re.I)
LEARN_DIR_RE = re.compile(r"(?:[-_]learn)$")


@dataclass(frozen=True)
class PlanItem:
    old_dir: Path
    new_dir: Path
    old_rel: str
    new_rel: str
    github_url: str


def normalize_repo_name(repo: str) -> str:
    repo = repo.rstrip(").,]\"'<>")
    if repo.endswith(".git"):
        repo = repo[:-4]
    return repo.strip("/")


def parse_github_ref(readme: Path) -> tuple[str, str, str]:
    text = readme.read_text(encoding="utf-8", errors="ignore")
    match = GITHUB_RE.search(text)
    if not match:
        raise ValueError(f"missing GitHub URL: {readme}")
    owner = match.group("owner")
    repo = normalize_repo_name(match.group("repo"))
    return owner, repo, f"https://github.com/{owner}/{repo}"


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def collect_plan(repo_root: Path) -> list[PlanItem]:
    items: list[PlanItem] = []
    for readme in sorted(repo_root.glob("*/*/*/README.md")):
        learn_dir = readme.parent
        if not LEARN_DIR_RE.search(learn_dir.name):
            continue
        if not learn_dir.is_dir():
            continue
        if not readme.is_file():
            continue
        owner, repo, github_url = parse_github_ref(readme)
        new_name = f"{owner}-{repo}-learn"
        if learn_dir.name == new_name:
            continue
        new_dir = learn_dir.with_name(new_name)
        items.append(
            PlanItem(
                old_dir=learn_dir,
                new_dir=new_dir,
                old_rel=rel(learn_dir, repo_root),
                new_rel=rel(new_dir, repo_root),
                github_url=github_url,
            )
        )
    return items


def validate_plan(items: list[PlanItem]) -> list[str]:
    errors: list[str] = []
    targets: dict[Path, PlanItem] = {}
    sources = {item.old_dir for item in items}
    for item in items:
        if item.new_dir in targets:
            errors.append(f"duplicate-target\t{item.new_rel}\t{item.old_rel}\t{targets[item.new_dir].old_rel}")
        targets[item.new_dir] = item
        if item.new_dir.exists() and item.new_dir not in sources:
            errors.append(f"target-exists\t{item.new_rel}\tfrom={item.old_rel}")
    return errors


def update_root_readme(repo_root: Path, items: list[PlanItem]) -> None:
    root_readme = repo_root / "README.md"
    text = root_readme.read_text(encoding="utf-8")
    for item in items:
        text = text.replace(f'./{item.old_rel}', f'./{item.new_rel}')
    root_readme.write_text(text, encoding="utf-8")


def apply_plan(repo_root: Path, items: list[PlanItem]) -> None:
    update_root_readme(repo_root, items)
    for item in items:
        item.old_dir.rename(item.new_dir)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root")
    parser.add_argument("--apply", action="store_true", help="rename directories and update root README")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).expanduser().resolve()
    items = collect_plan(repo_root)
    errors = validate_plan(items)

    if errors:
        print(f"ERROR\t{len(errors)} conflict(s)")
        for error in errors:
            print(error)
        return 2

    if not items:
        print("NO_CHANGES")
        return 0

    mode = "APPLY" if args.apply else "DRY_RUN"
    print(f"{mode}\t{len(items)} rename(s)")
    for item in items:
        print(f"{item.old_rel}\t=>\t{item.new_rel}\t{item.github_url}")

    if args.apply:
        apply_plan(repo_root, items)
        print("DONE")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
