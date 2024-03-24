from youtubei._registries import WEB_REGISTRY

from ._base import BaseRenderer

__all__ = ("UnifiedSharePanelRenderer",)


@WEB_REGISTRY
class UnifiedSharePanelRenderer(BaseRenderer):
    show_loading_spinner: bool
