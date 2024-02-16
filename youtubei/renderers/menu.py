from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY

from ._base import BaseRenderer

@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class MenuRenderer(BaseRenderer):
    open_immediately: bool
