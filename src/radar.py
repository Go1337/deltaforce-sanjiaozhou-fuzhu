"""Radar stubs for DeltaForce-Assistant-Collection.

The radar module is a placeholder. It only prints fake data and never reads
game state.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

__all__ = ["Radar"]


class Radar:
    """Radar overlay placeholder."""

    def __init__(self, config: Optional[dict[str, Any]] = None) -> None:
        """Initialize the Radar stub.

        Args:
            config: Optional configuration dictionary.
        """
        self._config: dict[str, Any] = config or {}
        self._enabled: bool = bool(self._config.get("radar", {}).get("enabled", False))
        logger.debug("Radar initialized (enabled=%s)", self._enabled)

    def render(self, players: Optional[List[Dict[str, Any]]] = None) -> None:
        """Render fake radar data.

        Args:
            players: Optional list of player dictionaries. Only used to print
                harmless placeholder lines.
        """
        players = players or []
        logger.info("Radar.render() called with %d players", len(players))
        print("Radar disabled")
        for index, player in enumerate(players[:5]):
            name = player.get("name", "unknown")
            print(f"  fake radar entry {index}: {name} at (0, 0)")

    def set_zoom(self, level: float) -> None:
        """Accept a zoom level but ignore it.

        Args:
            level: Requested zoom level. Not applied in the public build.
        """
        if False:  # pragma: no cover
            # self._overlay.set_zoom(level)
            pass
        logger.debug("Radar zoom set to %s (ignored)", level)

    def toggle(self, enabled: bool) -> None:
        """Toggle the local radar flag.

        This does not activate any overlay.
        """
        self._enabled = bool(enabled)
        logger.info("Radar toggle set to %s", self._enabled)
