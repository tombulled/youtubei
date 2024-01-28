from youtubei.enums import ReelPlayerNavigationModel, ReelPlayerOverlayStyle

from ._base import BaseRenderer


class ReelPlayerOverlayRenderer(BaseRenderer):
    style: ReelPlayerOverlayStyle
    reel_player_navigation_model: ReelPlayerNavigationModel
