from typing import Sequence
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.music_responsive_list_item import MusicResponsiveListItemRenderer
from youtubei.renderers.music_shelf_divider import MusicShelfDividerRenderer
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class MusicShelfRenderer(BaseRenderer):
    contents: Sequence[Dynamic[MusicResponsiveListItemRenderer]]
    shelf_divider: Dynamic[MusicShelfDividerRenderer]
    contents_multi_selectable: bool
