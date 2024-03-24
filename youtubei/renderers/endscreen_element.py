from typing import Any, Optional, Sequence

from youtubei.enums import EndscreenElementStyle
from youtubei.models.text import Text
from youtubei.models.thumbnail import Thumbnails
from youtubei.parse import Dynamic
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("EndscreenElementRenderer",)


class EndscreenElementRenderer(BaseRenderer):
    style: EndscreenElementStyle
    image: Thumbnails
    left: float
    width: float
    top: float
    aspect_ratio: float
    start_ms: str
    end_ms: str
    title: Text
    metadata: Text
    endpoint: DynamicCommand[Any]
    id: str
    thumbnail_overlays: Optional[Sequence[Dynamic[Any]]] = (
        None  # Observed: Sequence[ThumbnailOverlayTimeStatusRenderer]
    )
    playlist_length: Optional[Text] = None
