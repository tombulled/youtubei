from youtubei._registries import WEB_REGISTRY
from youtubei.enums import ThumbnailOverlayTimeStatusStyle
from youtubei.models.text import Text

from ._base import BaseRenderer

__all__ = ("ThumbnailOverlayTimeStatusRenderer",)


@WEB_REGISTRY
class ThumbnailOverlayTimeStatusRenderer(BaseRenderer):
    text: Text
    style: ThumbnailOverlayTimeStatusStyle
