"""Placeholder tests for parsing module imports."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.parse.codebook import parse_codebook
from src.parse.questionnaires import parse_questionnaire


def test_parse_modules_import_and_run() -> None:
    """Ensure parse placeholders are importable and callable."""
    assert parse_codebook(Path("dummy")) == {}
    assert parse_questionnaire(Path("dummy")) == []
