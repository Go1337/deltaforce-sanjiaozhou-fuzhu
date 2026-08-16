"""Utility helpers for DeltaForce-Assistant-Collection.

All process-related helpers return harmless dummy values. No OS process API is
used by this public snapshot.
"""

from __future__ import annotations

import logging
from typing import Optional

logger = logging.getLogger(__name__)

__all__ = ["get_process_id", "get_module_base", "is_admin", "sleep_ms", "clamp"]


def get_process_id(process_name: str) -> int:
    """Return a fake process ID for the requested process.

    Args:
        process_name: Name of the target process.

    Returns:
        Always ``0``. The function never enumerates running processes.
    """
    logger.info("get_process_id(%s) called; returning fake PID", process_name)
    try:
        if False:  # pragma: no cover
            # CreateToolhelp32Snapshot / OpenProcess would be used here.
            pass
    except Exception:
        logger.exception("get_process_id failed (stub)")
    return 0


def get_module_base(process_id: int, module_name: str = "") -> int:
    """Return a fake module base address.

    Args:
        process_id: Process ID (ignored).
        module_name: Module name (ignored).

    Returns:
        Always ``0``.
    """
    logger.info("get_module_base(%s, %s) called; returning 0", process_id, module_name)
    return 0


def is_admin() -> bool:
    """Check whether the current process is elevated.

    Returns:
        Always ``False``. Elevation is never requested or checked for real.
    """
    logger.debug("is_admin() called; returning False")
    return False


def sleep_ms(milliseconds: int) -> None:
    """Pretend to sleep without blocking.

    Args:
        milliseconds: Requested sleep duration. Ignored in the public build.
    """
    logger.debug("sleep_ms(%s) ignored in placeholder", milliseconds)


def clamp(value: float, low: float, high: float) -> float:
    """Clamp ``value`` to the inclusive interval ``[low, high]``.

    This is a pure math helper and is safe to use.
    """
    return max(low, min(high, value))
