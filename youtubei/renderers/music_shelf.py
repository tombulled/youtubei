from typing import Optional, Sequence

from youtubei.models.data import NextContinuationData
from youtubei.models.endpoints import SearchEndpoint
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.music_responsive_list_item import (
    MusicResponsiveListItemRenderer,
)
from youtubei.renderers.music_shelf_divider import MusicShelfDividerRenderer
from youtubei.validated_types import DynamicCommand

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicShelfRenderer",)


@WEB_REMIX_REGISTRY
class MusicShelfRenderer(BaseRenderer):
    contents: Sequence[Dynamic[MusicResponsiveListItemRenderer]]
    shelf_divider: Dynamic[MusicShelfDividerRenderer]
    contents_multi_selectable: Optional[bool] = None
    title: Optional[ComplexText] = None
    bottom_text: Optional[ComplexText] = None
    bottom_endpoint: Optional[DynamicCommand[SearchEndpoint]] = None
    continuations: Optional[Sequence[Dynamic[NextContinuationData]]] = None
