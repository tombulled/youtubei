from youtubei.enums import ThumbnailOverlayTimeStatusStyle
from youtubei.models.text import Text

from ._base import BaseRenderer


class ThumbnailOverlayTimeStatusRenderer(BaseRenderer):
    text: Text
    style: ThumbnailOverlayTimeStatusStyle
