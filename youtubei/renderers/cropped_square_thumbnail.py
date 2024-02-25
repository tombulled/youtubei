from youtubei.models.thumbnail import Thumbnails
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY

@WEB_REMIX_REGISTRY
class CroppedSquareThumbnailRenderer(BaseRenderer):
    thumbnail: Thumbnails