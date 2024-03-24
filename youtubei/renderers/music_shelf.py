from typing import Sequence

from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.music_responsive_list_item import (
    MusicResponsiveListItemRenderer,
)
from youtubei.renderers.music_shelf_divider import MusicShelfDividerRenderer

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicShelfRenderer",)


@WEB_REMIX_REGISTRY
class MusicShelfRenderer(BaseRenderer):
    contents: Sequence[Dynamic[MusicResponsiveListItemRenderer]]
    shelf_divider: Dynamic[MusicShelfDividerRenderer]
    contents_multi_selectable: bool
