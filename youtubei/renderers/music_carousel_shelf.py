from typing import Sequence
from youtubei.enums.other import CollectionStyleItemSize
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.music_carousel_shelf_basic_header import (
    MusicCarouselShelfBasicHeaderRenderer,
)
from youtubei.renderers.music_two_row_item import MusicTwoRowItemRenderer
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicCarouselShelfRenderer",)


@WEB_REMIX_REGISTRY
class MusicCarouselShelfRenderer(BaseRenderer):
    header: Dynamic[MusicCarouselShelfBasicHeaderRenderer]
    contents: Sequence[Dynamic[MusicTwoRowItemRenderer]]
    item_size: CollectionStyleItemSize
