"""Lightweight logging helper for codex session notes."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from src.config import project_root


def append_session_log(message: str, log_path: Path | None = None) -> Path:
    """Append a timestamped line to the codex session log file."""
    path = log_path or (project_root() / "docs" / "logs" / "codex-session-log.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"- [{timestamp}] {message}\n")
    return path
