from typing import Sequence

from youtubei._registries import WEB_REGISTRY
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.playlist_video import PlaylistVideoRenderer

from ._base import BaseRenderer

__all__ = ("PlaylistVideoListRenderer",)


@WEB_REGISTRY
class PlaylistVideoListRenderer(BaseRenderer):
    contents: Sequence[Dynamic[PlaylistVideoRenderer]]
    playlist_id: str
    is_editable: bool
    can_reorder: bool
    target_id: str
