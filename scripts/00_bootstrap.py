"""Bootstrap script for project scaffolding checks."""

from __future__ import annotations

from src.config import data_dir, outputs_dir
from src.utils.logging import append_session_log


def main() -> None:
    """Run project bootstrap placeholder actions."""
    print(f"[bootstrap] data dir: {data_dir()}")
    print(f"[bootstrap] outputs dir: {outputs_dir()}")
    append_session_log("Ran 00_bootstrap.py placeholder script.")


if __name__ == "__main__":
    main()
