from ._base import BaseRenderer

from youtubei._registries import WEB_REMIX_REGISTRY

@WEB_REMIX_REGISTRY
class MenuRenderer(BaseRenderer):
    open_immediately: bool
