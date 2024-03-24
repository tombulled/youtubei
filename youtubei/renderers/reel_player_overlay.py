from youtubei._registries import WEB_REGISTRY
from youtubei.enums import ReelPlayerNavigationModel, ReelPlayerOverlayStyle

from ._base import BaseRenderer

__all__ = ("ReelPlayerOverlayRenderer",)


@WEB_REGISTRY
class ReelPlayerOverlayRenderer(BaseRenderer):
    style: ReelPlayerOverlayStyle
    reel_player_navigation_model: ReelPlayerNavigationModel
