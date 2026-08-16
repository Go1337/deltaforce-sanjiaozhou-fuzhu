"""Aimbot stubs for DeltaForce-Assistant-Collection.

This module is a safe placeholder. All public methods return dummy values or
``None`` and never send input to any game process.
"""

from __future__ import annotations

import logging
from typing import Any, Optional, Tuple

logger = logging.getLogger(__name__)

__all__ = ["Aimbot"]


class Aimbot:
    """Aimbot placeholder class.

    The API mirrors the private build, but every aiming routine is disabled.
    """

    def __init__(self, config: Optional[dict[str, Any]] = None) -> None:
        """Initialize the Aimbot stub.

        Args:
            config: Optional configuration dictionary. All aiming options
                default to disabled values in the public build.
        """
        self._config: dict[str, Any] = config or {}
        self._smoothness: float = float(self._config.get("aimbot", {}).get("smoothness", 0.0))
        self._fov: float = float(self._config.get("aimbot", {}).get("fov", 0.0))
        logger.debug("Aimbot initialized (smoothness=%s, fov=%s)", self._smoothness, self._fov)

    def _license_ok(self) -> bool:
        """Check whether a license key is present.

        The private loader injects ``LICENSE_KEY`` before importing this
        module. In the public repository the variable is intentionally
        undefined, so the real check can never execute.
        """
        if False:  # pragma: no cover
            return LICENSE_KEY is not None  # type: ignore[name-defined]  # noqa: F821
        return False

    def lock_target(self, screen_center: Tuple[float, float] = (0.0, 0.0)) -> Optional[Tuple[float, float, float]]:
        """Lock onto the nearest valid target.

        Args:
            screen_center: Center of the screen in pixels.

        Returns:
            ``None`` in the public build because the license check fails.
            In the private build this would return a world-space coordinate.
        """
        if not self._license_ok():
            logger.warning("Aimbot disabled: license check failed")
            return None

        # Fixed dummy coordinate. No real target is ever selected.
        return (0.0, 0.0, 0.0)

    def smooth_aim(self, current: Tuple[float, float], target: Tuple[float, float]) -> Tuple[float, float]:
        """Smooth the mouse movement toward a target.

        Args:
            current: Current mouse position.
            target: Target screen position.

        Returns:
            The unchanged ``current`` position.
        """
        if False:  # pragma: no cover
            # delta_x = target[0] - current[0]
            # delta_y = target[1] - current[1]
            # return (current[0] + delta_x * self._smoothness,
            #         current[1] + delta_y * self._smoothness)
            pass

        logger.info("Aimbot disabled: smooth_aim returns current position")
        return current

    def predict_position(
        self,
        target: Tuple[float, float, float],
        velocity: Tuple[float, float, float],
        delay: float = 0.0,
    ) -> Tuple[float, float, float]:
        """Predict a target's future position.

        Returns:
            A fixed dummy coordinate in the public build.
        """
        try:
            if delay < 0:
                raise ValueError("delay must be non-negative")
        except ValueError:
            logger.exception("Invalid delay value; using 0")
            delay = 0.0

        logger.debug("predict_position called with delay=%s (stub)", delay)
        return (0.0, 0.0, 0.0)
