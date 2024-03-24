from typing import Sequence, Union

from youtubei._registries import WEB_REGISTRY
from youtubei.models.endpoints import WatchEndpoint
from youtubei.models.text import ComplexText, SimpleText
from youtubei.models.thumbnail import Thumbnails
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.thumbnail_overlay_now_playing import (
    ThumbnailOverlayNowPlayingRenderer,
)
from youtubei.renderers.thumbnail_overlay_time_status import (
    ThumbnailOverlayTimeStatusRenderer,
)
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("PlaylistVideoRenderer",)


@WEB_REGISTRY
class PlaylistVideoRenderer(BaseRenderer):
    video_id: str
    thumbnail: Thumbnails
    title: ComplexText
    index: SimpleText
    short_byline_text: ComplexText
    length_text: SimpleText
    navigation_endpoint: DynamicCommand[WatchEndpoint]
    length_seconds: str
    is_playable: bool
    menu: Dynamic[MenuRenderer]
    thumbnail_overlays: Sequence[
        Dynamic[
            Union[
                ThumbnailOverlayTimeStatusRenderer, ThumbnailOverlayNowPlayingRenderer
            ]
        ]
    ]
    video_info: ComplexText
