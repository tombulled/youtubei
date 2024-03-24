from typing import Sequence

from ._base import BaseModel

__all__ = (
    "VerticalGradient",
    "MusicItemThumbnailOverlayBackground",
    "PlaylistItemData",
)


class VerticalGradient(BaseModel):
    gradient_layer_colors: Sequence[str]


class MusicItemThumbnailOverlayBackground(BaseModel):
    vertical_gradient: VerticalGradient


class PlaylistItemData(BaseModel):
    playlist_set_video_id: str
    video_id: str
