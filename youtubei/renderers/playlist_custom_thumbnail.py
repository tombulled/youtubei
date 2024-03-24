from youtubei._registries import WEB_REGISTRY
from youtubei.models.thumbnail import Thumbnails

from ._base import BaseRenderer

__all__ = ("PlaylistCustomThumbnailRenderer",)


@WEB_REGISTRY
class PlaylistCustomThumbnailRenderer(BaseRenderer):
    thumbnail: Thumbnails
