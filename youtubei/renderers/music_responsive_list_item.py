from typing import Optional, Sequence

from youtubei.enums.music import (
    MusicResponsiveListItemFlexColumnDisplayStyle,
    MusicResponsiveListItemHeight,
)
from youtubei.models.endpoints import BrowseEndpoint
from youtubei.models.music import PlaylistItemData
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.checkbox import CheckboxRenderer
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.music_inline_badge import MusicInlineBadgeRenderer
from youtubei.renderers.music_item_thumbnail_overlay import (
    MusicItemThumbnailOverlayRenderer,
)
from youtubei.renderers.music_responsive_list_item_fixed_column import (
    MusicResponsiveListItemFixedColumnRenderer,
)
from youtubei.renderers.music_responsive_list_item_flex_column import (
    MusicResponsiveListItemFlexColumnRenderer,
)
from youtubei.renderers.music_thumbnail import MusicThumbnailRenderer
from youtubei.validated_types import DynamicCommand

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicResponsiveListItemRenderer",)


@WEB_REMIX_REGISTRY
class MusicResponsiveListItemRenderer(BaseRenderer):
    thumbnail: Optional[Dynamic[MusicThumbnailRenderer]] = None
    overlay: Optional[Dynamic[MusicItemThumbnailOverlayRenderer]] = None
    flex_columns: Sequence[Dynamic[MusicResponsiveListItemFlexColumnRenderer]]
    fixed_columns: Optional[
        Sequence[Dynamic[MusicResponsiveListItemFixedColumnRenderer]]
    ] = None
    menu: Dynamic[MenuRenderer]
    playlist_item_data: Optional[PlaylistItemData] = None
    item_height: Optional[MusicResponsiveListItemHeight] = None
    index: Optional[ComplexText] = None
    multi_select_checkbox: Optional[Dynamic[CheckboxRenderer]] = None
    navigation_endpoint: Optional[DynamicCommand[BrowseEndpoint]] = None
    flex_column_display_style: Optional[
        MusicResponsiveListItemFlexColumnDisplayStyle
    ] = None
    badges: Optional[Sequence[Dynamic[MusicInlineBadgeRenderer]]] = None
