from typing import Sequence

from youtubei.types import TrackingParams

from .base import BaseModel

__all__ = (
    "Thumbnail",
    "Thumbnails",
    "ThumbnailMapEntry",
    "ThemedThumbnail",
)


class Thumbnail(BaseModel):
    url: str
    width: int
    height: int


# Rename to `Image`?
class Thumbnails(BaseModel):
    thumbnails: Sequence[Thumbnail]


class ThumbnailMapEntry(BaseModel):
    key: str
    value: Thumbnails


class ThemedThumbnail(BaseModel):
    thumbnail_map: Sequence[ThumbnailMapEntry]


class AdThumbnail(BaseModel):
    thumbnail: Thumbnails
    tracking_params: TrackingParams
