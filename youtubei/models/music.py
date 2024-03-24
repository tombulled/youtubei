from typing import Sequence
from .base import BaseModel


class VerticalGradient(BaseModel):
    gradient_layer_colors: Sequence[str]


class MusicItemThumbnailOverlayBackground(BaseModel):
    vertical_gradient: VerticalGradient


class PlaylistItemData(BaseModel):
    playlist_set_video_id: str
    video_id: str
