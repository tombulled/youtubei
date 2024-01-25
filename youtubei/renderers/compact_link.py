from youtubei.models.base import BaseModel
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.types import TrackingParams


class CompactLinkRenderer(BaseModel):
    icon: Icon
    title: Text
    navigation_endpoint: NavigationEndpoint
    tracking_params: TrackingParams
