from youtubei.enums import ReelPlayerNavigationModel, ReelPlayerOverlayStyle
from youtubei.models.base import BaseModel
from ._base import BaseRenderer


class ReelPlayerOverlayRenderer(BaseRenderer):
    style: ReelPlayerOverlayStyle
    reel_player_navigation_model: ReelPlayerNavigationModel
