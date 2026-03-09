"""Project path configuration helpers."""

from __future__ import annotations

from pathlib import Path


def project_root(start: Path | None = None) -> Path:
    """Discover project root by locating `pyproject.toml` in parent paths."""
    current = (start or Path(__file__)).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "pyproject.toml").exists():
            return candidate
    raise FileNotFoundError("Could not find project root containing pyproject.toml")


def data_dir() -> Path:
    """Return the data directory path."""
    return project_root() / "data"


def outputs_dir() -> Path:
    """Return the outputs directory path."""
    return project_root() / "outputs"
