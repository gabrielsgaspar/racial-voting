"""CLI placeholder for ANES download workflow."""

from __future__ import annotations

from src.config import data_dir
from src.download.anes import download_anes_dataset
from src.utils.logging import append_session_log


def main() -> None:
    """Run placeholder ANES download entrypoint."""
    target = data_dir() / "raw" / "anes"
    download_anes_dataset(target)
    print(f"[download_anes] would download ANES data into: {target}")
    append_session_log("Ran 01_download_anes.py placeholder script (no external download).")


if __name__ == "__main__":
    main()
