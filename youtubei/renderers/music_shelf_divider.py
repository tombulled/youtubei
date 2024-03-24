from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicShelfDividerRenderer",)


@WEB_REMIX_REGISTRY
class MusicShelfDividerRenderer(BaseRenderer):
    hidden: bool
