from typing import Optional
from youtubei.enums import Style
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.types import TrackingParams
from ._base import BaseRenderer


class SimpleAdBadgeRenderer(BaseRenderer):
    text: Text  # ComplexText
    navigation_endpoint: Optional[NavigationEndpoint] = None
    tracking_params: TrackingParams
    icon: Optional[Icon] = None
    style: Optional[Style] = None
