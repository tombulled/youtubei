from youtubei._registries import WEB_REGISTRY
from youtubei.models.text import Text

from ._base import BaseRenderer


@WEB_REGISTRY
class PlaylistBylineRenderer(BaseRenderer):
    text: Text  # simple and complex
