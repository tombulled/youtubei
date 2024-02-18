from youtubei.enums import ThumbnailOverlayTimeStatusStyle
from youtubei.models.text import Text
from youtubei._registries import WEB_REGISTRY

from ._base import BaseRenderer

@WEB_REGISTRY
class ThumbnailOverlayTimeStatusRenderer(BaseRenderer):
    text: Text
    style: ThumbnailOverlayTimeStatusStyle
