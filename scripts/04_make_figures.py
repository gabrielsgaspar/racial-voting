"""CLI placeholder for figure generation workflow."""

from __future__ import annotations

from src.analysis.descriptives import run_descriptives
from src.analysis.figures import make_figures
from src.utils.logging import append_session_log


def main() -> None:
    """Run placeholder figure generation entrypoint."""
    run_descriptives()
    make_figures()
    print("[figures] would generate descriptive tables and figures")
    append_session_log("Ran 04_make_figures.py placeholder script.")


if __name__ == "__main__":
    main()
