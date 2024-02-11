from typing import Optional, Sequence

from youtubei.enums import EndscreenElementStyle
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.text import Text
from youtubei.models.thumbnail import Thumbnails
from youtubei.parse import Dynamic

from ._base import BaseRenderer


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
    endpoint: NavigationEndpoint  # Note: guess taken that this was a NaviationEndpoint, as the field name is ambiguous
    id: str
    thumbnail_overlays: Optional[Sequence[Dynamic]] = (
        None  # Sequence[ThumbnailOverlayTimeStatusRenderer]
    )
    playlist_length: Optional[Text] = None
