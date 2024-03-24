from youtubei.enums.music import MusicThumbnailCrop, MusicThumbnailScale
from youtubei.models.thumbnail import Thumbnails

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicThumbnailRenderer",)


@WEB_REMIX_REGISTRY
class MusicThumbnailRenderer(BaseRenderer):
    thumbnail: Thumbnails
    thumbnail_crop: MusicThumbnailCrop
    thumbnail_scale: MusicThumbnailScale
