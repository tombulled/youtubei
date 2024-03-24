from youtubei._registries import WEB_REGISTRY
from youtubei.models.endpoints import WatchEndpoint
from youtubei.models.thumbnail import Thumbnails
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.thumbnail_overlay_hover_text import (
    ThumbnailOverlayHoverTextRenderer,
)
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("HeroPlaylistThumbnailRenderer",)


@WEB_REGISTRY
class HeroPlaylistThumbnailRenderer(BaseRenderer):
    thumbnail: Thumbnails
    max_ratio: float
    on_tap: DynamicCommand[WatchEndpoint]
    thumbnail_overlays: Dynamic[ThumbnailOverlayHoverTextRenderer]
