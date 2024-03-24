from typing import Sequence

from youtubei._registries import WEB_REGISTRY
from youtubei.models.endpoints import WatchEndpoint
from youtubei.models.text import ComplexText, Text
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.metadata_badge import MetadataBadgeRenderer
from youtubei.renderers.playlist_custom_thumbnail import PlaylistCustomThumbnailRenderer
from youtubei.renderers.thumbnail_overlay_side_panel import (
    ThumbnailOverlaySidePanelRenderer,
)
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("PlaylistSidebarPrimaryInfoRenderer",)


@WEB_REGISTRY
class PlaylistSidebarPrimaryInfoRenderer(BaseRenderer):
    thumbnail_renderer: Dynamic[PlaylistCustomThumbnailRenderer]
    title: ComplexText
    stats: Sequence[Text]
    menu: Dynamic[MenuRenderer]
    thumbnail_overlays: Sequence[Dynamic[ThumbnailOverlaySidePanelRenderer]]
    navigation_endpoint: DynamicCommand[WatchEndpoint]
    badges: Sequence[Dynamic[MetadataBadgeRenderer]]
    show_more_text: ComplexText
