"""Utility helpers for download routines."""

from __future__ import annotations


def build_user_agent(app_name: str = "racial-voting") -> str:
    """Create a basic user-agent string for HTTP requests."""
    return f"{app_name}/0.1.0"
