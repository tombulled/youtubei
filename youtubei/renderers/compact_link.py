from typing import Optional
from youtubei.models.base import BaseModel
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.types import TrackingParams
from ._base import BaseRenderer


class CompactLinkRenderer(BaseRenderer):
    icon: Icon
    title: Text
    navigation_endpoint: NavigationEndpoint
    shouldTintIcon: Optional[bool] = None
