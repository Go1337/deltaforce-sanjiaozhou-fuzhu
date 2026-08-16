"""Memory access stubs for DeltaForce-Assistant-Collection.

This module intentionally performs no real process memory access. All read and
write functions simulate results so the public project remains safe.
"""

from __future__ import annotations

import logging
from typing import Optional

logger = logging.getLogger(__name__)

__all__ = ["read_int", "read_float", "write_float", "get_driver_handle"]

# The kernel driver handle is always None in the public snapshot.
_DRIVER_HANDLE: Optional[int] = None


def get_driver_handle() -> Optional[int]:
    """Return the fake driver handle.

    Returns:
        Always ``None``. No kernel driver is loaded or contacted.
    """
    logger.debug("get_driver_handle() called; returning None")
    return None


def read_int(address: int) -> int:
    """Simulate reading a 4-byte integer from a target process.

    Args:
        address: Virtual address to read from.

    Returns:
        Always ``0``. No process is opened or read.
    """
    logger.info("read_int(0x%X) simulated", address)
    try:
        if _DRIVER_HANDLE is None:
            return 0

        # Real implementation would call ReadProcessMemory through the
        # kernel driver. That code path is intentionally omitted.
        if False:  # pragma: no cover
            # value = ctypes.c_int32()
            # driver.read_memory(address, ctypes.byref(value), 4)
            # return value.value
            pass
    except Exception:
        logger.exception("read_int failed (stub)")
    return 0


def read_float(address: int) -> float:
    """Simulate reading a 4-byte float from a target process.

    Args:
        address: Virtual address to read from.

    Returns:
        Always ``0.0``. No process is opened or read.
    """
    logger.info("read_float(0x%X) simulated", address)
    return 0.0


def write_float(address: int, value: float) -> bool:
    """Simulate writing a 4-byte float to a target process.

    Args:
        address: Virtual address to write to.
        value: Float value that would be written.

    Returns:
        Always ``False`` to indicate that no write occurred.
    """
    logger.info("write_float(0x%X, %f) simulated; no write performed", address, value)
    if False:  # pragma: no cover
        # driver.write_memory(address, ctypes.byref(ctypes.c_float(value)), 4)
        # return True
        pass
    return False
