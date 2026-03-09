"""CLI placeholder for ANES cleaning workflow."""

from __future__ import annotations

from src.transform.clean_core import clean_core_records
from src.transform.derive_vars import derive_variables
from src.transform.weights_design import apply_weights_design
from src.utils.logging import append_session_log


def main() -> None:
    """Run placeholder ANES cleaning entrypoint."""
    clean_core_records()
    derive_variables()
    apply_weights_design()
    print("[clean_anes] would run clean + derive + weights workflow")
    append_session_log("Ran 03_clean_anes.py placeholder script.")


if __name__ == "__main__":
    main()
