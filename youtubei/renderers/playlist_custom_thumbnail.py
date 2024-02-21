from youtubei._registries import WEB_REGISTRY
from youtubei.models.thumbnail import Thumbnails

from ._base import BaseRenderer


@WEB_REGISTRY
class PlaylistCustomThumbnailRenderer(BaseRenderer):
    thumbnail: Thumbnails
