from typing import Sequence

from ._base import BaseModel

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


class Thumbnails(BaseModel):
    thumbnails: Sequence[Thumbnail]


class ThumbnailMapEntry(BaseModel):
    key: str
    value: Thumbnails


class ThemedThumbnail(BaseModel):
    thumbnail_map: Sequence[ThumbnailMapEntry]
