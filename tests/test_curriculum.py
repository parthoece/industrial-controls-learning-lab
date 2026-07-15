from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_all_weekly_lessons_exist() -> None:
    lessons = sorted((ROOT / "learning").glob("week-*.md"))
    assert len(lessons) == 18


def test_lessons_have_required_sections() -> None:
    required = [
        "## Learning objectives",
        "## Key terms",
        "## Mental model",
        "## Worked example",
        "## Common mistakes",
        "## Practice",
        "## Knowledge checks",
        "## Deep study",
        "## Exit criteria",
    ]
    for lesson in sorted((ROOT / "learning").glob("week-*.md")):
        text = lesson.read_text(encoding="utf-8")
        for heading in required:
            assert heading in text, f"{lesson.name} missing {heading}"


def test_module_reviews_exist() -> None:
    reviews = sorted((ROOT / "learning" / "reviews").glob("module-*-review.md"))
    assert len(reviews) == 6
