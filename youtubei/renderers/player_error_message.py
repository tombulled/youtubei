from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.models.thumbnail import Thumbnails

from ._base import BaseRenderer

__all__ = ("PlayerErrorMessageRenderer",)


class PlayerErrorMessageRenderer(BaseRenderer):
    reason: Text
    thumbnail: Thumbnails
    icon: Icon
