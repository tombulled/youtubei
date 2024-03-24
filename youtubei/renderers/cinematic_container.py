from typing import Sequence

from youtubei._registries import WEB_REGISTRY
from youtubei.models.config import (
    BackgroundImageConfig,
    CinematicContainerConfig,
    ColourConfig,
)

from ._base import BaseRenderer

__all__ = ("CinematicContainerRenderer",)


@WEB_REGISTRY
class CinematicContainerRenderer(BaseRenderer):
    background_image_config: BackgroundImageConfig
    gradientColorConfig: Sequence[ColourConfig]
    config: CinematicContainerConfig
