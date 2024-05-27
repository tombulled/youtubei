from youtubei.models.text import ComplexText
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicCardShelfHeaderBasicRenderer",)


@WEB_REMIX_REGISTRY
class MusicCardShelfHeaderBasicRenderer(BaseRenderer):
    title: ComplexText
