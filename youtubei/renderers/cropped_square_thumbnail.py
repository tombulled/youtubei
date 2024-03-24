from youtubei.models.thumbnail import Thumbnails

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("CroppedSquareThumbnailRenderer",)


@WEB_REMIX_REGISTRY
class CroppedSquareThumbnailRenderer(BaseRenderer):
    thumbnail: Thumbnails
