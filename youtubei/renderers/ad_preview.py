from typing import Optional

from youtubei.models.other import AdTemplatedCountdown
from youtubei.models.text import Text
from youtubei.models.thumbnail import AdThumbnail

from ._base import BaseRenderer

__all__ = ("AdPreviewRenderer",)


class AdPreviewRenderer(BaseRenderer):
    thumbnail: Optional[AdThumbnail] = None
    duration_milliseconds: Optional[int] = None
    templated_countdown: Optional[AdTemplatedCountdown] = None
    static_preview: Optional[Text] = None  # Observed: TemplatedText
