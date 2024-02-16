from typing import Optional, Sequence

from youtubei.models.colour import Colour, ColourPalette
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
    sampled_thumbnail_color: Optional[Colour] = None
    dark_color_palette: Optional[ColourPalette] = None
    vibrant_color_palette: Optional[ColourPalette] = None


class ThumbnailMapEntry(BaseModel):
    key: str
    value: Thumbnails


class ThemedThumbnail(BaseModel):
    thumbnail_map: Sequence[ThumbnailMapEntry]


class AdThumbnail(BaseModel):
    thumbnail: Thumbnails
    tracking_params: TrackingParams
