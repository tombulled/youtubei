from youtubei._registries import WEB_REGISTRY
from youtubei.models.other import Icon
from youtubei.models.text import SimpleText

from ._base import BaseRenderer

__all__ = ("ThumbnailOverlayHoverTextRenderer",)


@WEB_REGISTRY
class ThumbnailOverlayHoverTextRenderer(BaseRenderer):
    text: SimpleText
    icon: Icon
