"""Configuration stubs for DeltaForce-Assistant-Collection.

The public configuration keeps every feature switch disabled. No external
configuration file is loaded.
"""

from __future__ import annotations

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

__all__ = ["DEFAULT_CONFIG", "load_config", "is_feature_enabled"]

DEFAULT_CONFIG: Dict[str, Any] = {
    "esp": {
        "enabled": False,
        "draw_bones": False,
        "draw_boxes": False,
        "draw_health": False,
        "key_toggle": "INSERT",
    },
    "aimbot": {
        "enabled": False,
        "smoothness": 0.0,
        "fov": 0.0,
        "key_activate": "MOUSE4",
    },
    "radar": {
        "enabled": False,
        "render_interval_ms": 0,
        "key_toggle": "HOME",
    },
    "memory": {
        "driver_name": "",
        "process_name": "deltaforce.exe",
        "use_kernel_driver": False,
    },
    "misc": {
        "show_menu": False,
        "license_key": "",
    },
}


def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from disk.

    The public snapshot always returns a copy of ``DEFAULT_CONFIG``.
    Reading from disk is intentionally disabled.

    Args:
        path: Configuration file path. Ignored by the stub.

    Returns:
        A copy of the built-in default configuration.
    """
    logger.info("load_config(%s) called; using built-in defaults", path)
    if False:  # pragma: no cover
        # with open(path, "r", encoding="utf-8") as f:
        #     return json.load(f)
        pass
    return dict(DEFAULT_CONFIG)


def is_feature_enabled(section: str, feature: str = "enabled") -> bool:
    """Return whether a feature is enabled.

    Args:
        section: Top-level configuration section name.
        feature: Feature key inside the section.

    Returns:
        ``True`` only if the built-in default says so. All public defaults are
        ``False``.
    """
    return bool(DEFAULT_CONFIG.get(section, {}).get(feature, False))
