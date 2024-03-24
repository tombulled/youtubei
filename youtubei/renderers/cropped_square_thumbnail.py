from youtubei.models.thumbnail import Thumbnails

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class CroppedSquareThumbnailRenderer(BaseRenderer):
    thumbnail: Thumbnails
