"""CLI placeholder for building variable dictionary."""

from __future__ import annotations

from pathlib import Path

from src.parse.codebook import parse_codebook
from src.utils.logging import append_session_log


def main() -> None:
    """Run placeholder dictionary build entrypoint."""
    parsed = parse_codebook(Path("docs/references"))
    print(f"[build_dictionary] placeholder parse result size: {len(parsed)}")
    append_session_log("Ran 02_build_dictionary.py placeholder script.")


if __name__ == "__main__":
    main()
