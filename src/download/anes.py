"""ANES download workflow placeholders."""

from __future__ import annotations

from pathlib import Path


def download_anes_dataset(target_dir: Path) -> Path:
    """Placeholder download function for ANES data."""
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir
