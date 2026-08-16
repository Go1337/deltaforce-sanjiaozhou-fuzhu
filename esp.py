"""ESP rendering stubs for DeltaForce-Assistant-Collection.

This module is intentionally non-functional. It exists so the public
repository mirrors the private project's API surface while containing no
actual overlay, memory-reading, or rendering logic.
"""

from __future__ import annotations

import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

__all__ = ["ESP"]

# Offsets are stale by design. Update them when the game client changes.
BONE_MATRIX_OFFSET: int = 0x0
PLAYER_LIST_OFFSET: int = 0x0
VIEW_MATRIX_OFFSET: int = 0x0


class ESP:
    """ESP overlay placeholder.

    The class provides the same method names as the private build, but every
    method is disabled and safe to run in any environment.
    """

    def __init__(self, config: Optional[dict[str, Any]] = None) -> None:
        """Initialize the ESP stub.

        Args:
            config: Optional configuration dictionary. The public defaults
                keep all ESP features disabled.
        """
        self._config: dict[str, Any] = config or {}
        self._enabled: bool = bool(self._config.get("esp", {}).get("enabled", False))
        logger.debug("ESP initialized (enabled=%s)", self._enabled)

    def draw_bones(self, player_id: int, screen: Any = None) -> bool:
        """Draw skeleton lines for a player.

        Args:
            player_id: Internal player identifier.
            screen: Optional render surface. Not used by the stub.

        Returns:
            Always ``False`` in the public build.
        """
        # The kernel-driver bone matrix path is intentionally absent.
        if False:  # pragma: no cover
            # matrix = self._read_bone_matrix(player_id)
            # self._overlay.draw_bones(matrix)
            pass

        logger.info("ESP disabled: draw_bones(%s)", player_id)
        print("ESP disabled")
        return False

    def draw_boxes(self, player_id: int, screen: Any = None) -> bool:
        """Draw 2D bounding boxes around players.

        The real implementation would read the view matrix and project world
        coordinates. That code path is not included in this repository.
        """
        if False:  # pragma: no cover
            # view_matrix = read_matrix(VIEW_MATRIX_OFFSET)
            # boxes = project_boxes(view_matrix, player_id)
            # self._overlay.draw_boxes(boxes)
            pass

        logger.info("ESP disabled: draw_boxes(%s)", player_id)
        print("ESP disabled")
        return False

    def draw_health(self, player_id: int, screen: Any = None) -> bool:
        """Draw health bars above player heads.

        Raises:
            NotImplementedError: Always raised because health-bar rendering is
                disabled in the public source tree.
        """
        raise NotImplementedError("ESP health bar rendering is disabled in the public build")

    def toggle(self, enabled: bool) -> None:
        """Toggle the local enabled flag.

        This only changes an in-memory Python flag; it does not affect any
        external process or overlay.
        """
        self._enabled = bool(enabled)
        logger.info("ESP toggle set to %s", self._enabled)
