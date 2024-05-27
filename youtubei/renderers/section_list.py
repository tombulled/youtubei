from typing import Optional, Sequence, Union

from youtubei._registries import ANDROID_REGISTRY, WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.data import NextContinuationData
from youtubei.parse import Dynamic
from youtubei.renderers.chip_cloud import ChipCloudRenderer
from youtubei.renderers.item_section import ItemSectionRenderer
from youtubei.renderers.music_card_shelf import MusicCardShelfRenderer
from youtubei.renderers.music_carousel_shelf import MusicCarouselShelfRenderer
from youtubei.renderers.music_playlist_shelf import MusicPlaylistShelfRenderer
from youtubei.renderers.music_shelf import MusicShelfRenderer

from ._base import BaseRenderer

__all__ = ("SectionListRenderer",)


@WEB_REMIX_REGISTRY
@WEB_REGISTRY
@ANDROID_REGISTRY
class SectionListRenderer(BaseRenderer):
    contents: Sequence[
        Dynamic[
            Union[
                ItemSectionRenderer,
                MusicPlaylistShelfRenderer,
                MusicCarouselShelfRenderer,
                MusicShelfRenderer,
                MusicCardShelfRenderer,
            ]
        ]
    ]
    continuations: Optional[Sequence[Dynamic[NextContinuationData]]] = None
    header: Optional[Dynamic[ChipCloudRenderer]] = None
