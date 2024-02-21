from youtubei._registries import WEB_REGISTRY
from youtubei.models.text import ComplexText

from ._base import BaseRenderer


@WEB_REGISTRY
class ThumbnailOverlayNowPlayingRenderer(BaseRenderer):
    text: ComplexText
