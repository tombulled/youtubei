from youtubei.enums import ReelPlayerNavigationModel, ReelPlayerOverlayStyle
from youtubei.models.base import BaseModel


class ReelPlayerOverlayRenderer(BaseModel):
    style: ReelPlayerOverlayStyle
    tracking_params: str
    reel_player_navigation_model: ReelPlayerNavigationModel
