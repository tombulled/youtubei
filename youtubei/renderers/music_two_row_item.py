from typing import Sequence
from youtubei.enums.music import MusicTwoRowItemThumbnailAspectRatio
from youtubei.models.endpoints import BrowseEndpoint
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.music_inline_badge import MusicInlineBadgeRenderer
from youtubei.renderers.music_item_thumbnail_overlay import (
    MusicItemThumbnailOverlayRenderer,
)
from youtubei.renderers.music_thumbnail import MusicThumbnailRenderer
from youtubei.validated_types import DynamicCommand
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicTwoRowItemRenderer",)


@WEB_REMIX_REGISTRY
class MusicTwoRowItemRenderer(BaseRenderer):
    thumbnail_renderer: Dynamic[MusicThumbnailRenderer]
    aspect_ratio: MusicTwoRowItemThumbnailAspectRatio
    title: ComplexText
    subtitle: ComplexText
    navigation_endpoint: DynamicCommand[BrowseEndpoint]
    menu: Dynamic[MenuRenderer]
    thumbnail_overlay: Dynamic[MusicItemThumbnailOverlayRenderer]
    subtitle_badges: Sequence[Dynamic[MusicInlineBadgeRenderer]]
