from typing import Optional, Sequence

from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.music_responsive_list_item import MusicResponsiveListItemRenderer
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class MusicPlaylistShelfRenderer(BaseRenderer):
    playlist_id: Optional[str] = None
    contents: Sequence[Dynamic[MusicResponsiveListItemRenderer]]
    collapsed_item_count: int
    contents_multi_selectable: bool
