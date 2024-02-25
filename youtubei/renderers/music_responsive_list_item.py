from typing import Sequence
from youtubei.models.music import PlaylistItemData
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.checkbox import CheckboxRenderer
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.music_item_thumbnail_overlay import MusicItemThumbnailOverlayRenderer
from youtubei.renderers.music_responsive_list_item_fixed_column import MusicResponsiveListItemFixedColumnRenderer
from youtubei.renderers.music_responsive_list_item_flex_column import MusicResponsiveListItemFlexColumnRenderer
from youtubei.renderers.music_thumbnail import MusicThumbnailRenderer
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class MusicResponsiveListItemRenderer(BaseRenderer):
    thumbnail: Dynamic[MusicThumbnailRenderer]
    overlay: Dynamic[MusicItemThumbnailOverlayRenderer]
    flex_columns: Sequence[Dynamic[MusicResponsiveListItemFlexColumnRenderer]]
    fixed_columns: Sequence[Dynamic[MusicResponsiveListItemFixedColumnRenderer]]
    menu: Dynamic[MenuRenderer]
    playlist_item_data: PlaylistItemData
    multi_select_checkbox: Dynamic[CheckboxRenderer]
