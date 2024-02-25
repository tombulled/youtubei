from typing import Sequence, Union

from youtubei._registries import ANDROID_REGISTRY, WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.item_section import ItemSectionRenderer
from youtubei.renderers.music_playlist_shelf import MusicPlaylistShelfRenderer

from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
@WEB_REGISTRY
@ANDROID_REGISTRY
class SectionListRenderer(BaseRenderer):
    contents: Sequence[
        Dynamic[
            Union[
                ItemSectionRenderer,
                MusicPlaylistShelfRenderer,
            ]
        ]
    ]
