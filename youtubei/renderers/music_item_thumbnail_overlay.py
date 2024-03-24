from youtubei.enums.music import (
    MusicItemThumbnailOverlayContentPosition,
    MusicItemThumbnailOverlayDisplayStyle,
)
from youtubei.models.music import MusicItemThumbnailOverlayBackground
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.music_play_button import MusicPlayButtonRenderer

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicItemThumbnailOverlayRenderer",)


@WEB_REMIX_REGISTRY
class MusicItemThumbnailOverlayRenderer(BaseRenderer):
    background: MusicItemThumbnailOverlayBackground
    content: Dynamic[MusicPlayButtonRenderer]
    content_position: MusicItemThumbnailOverlayContentPosition
    display_style: MusicItemThumbnailOverlayDisplayStyle
