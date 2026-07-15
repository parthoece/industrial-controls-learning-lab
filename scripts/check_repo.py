from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "NOTICE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "MAINTAINERS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "learning/README.md",
    "learning/references/deep-study.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/ci.yml",
]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def check_required_files() -> list[str]:
    return [f"missing required file: {path}" for path in REQUIRED if not (ROOT / path).exists()]


def check_relative_links() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            target = target.strip().split("#", 1)[0]
            if (
                not target
                or target.startswith(("http://", "https://", "mailto:"))
                or target.endswith("_URL")
            ):
                continue
            destination = (markdown.parent / target).resolve()
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{markdown.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{markdown.relative_to(ROOT)}: broken relative link: {target}")
    return errors


def check_for_generated_files() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []

    forbidden_parts = {"__pycache__", ".pytest_cache", ".venv"}
    return [
        f"generated path should not be committed: {tracked}"
        for tracked in result.stdout.splitlines()
        if any(part in forbidden_parts for part in Path(tracked).parts)
    ]


def check_curriculum_counts() -> list[str]:
    errors: list[str] = []
    lessons = list((ROOT / "learning").glob("week-*.md"))
    reviews = list((ROOT / "learning" / "reviews").glob("module-*-review.md"))
    if len(lessons) != 18:
        errors.append(f"expected 18 weekly lessons, found {len(lessons)}")
    if len(reviews) != 6:
        errors.append(f"expected 6 module reviews, found {len(reviews)}")
    return errors


def main() -> int:
    errors = (
        check_required_files()
        + check_relative_links()
        + check_for_generated_files()
        + check_curriculum_counts()
    )
    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository structure, curriculum, and relative links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
