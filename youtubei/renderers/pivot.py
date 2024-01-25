from typing import Optional, Sequence

from youtubei.enums import TargetId
from youtubei.models.accessibility import Accessibility
from youtubei.models.base import BaseModel
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.types import Renderer


class PivotBarItemRenderer(BaseModel):
    pivot_identifier: str
    navigation_endpoint: NavigationEndpoint
    title: Text
    accessibility: Accessibility
    icon: Icon
    tracking_params: str
    target_id: TargetId
    progress_indicator: Optional[Renderer] = None


class PivotBarRenderer(BaseModel):
    tracking_params: str
    items: Sequence[Renderer[PivotBarItemRenderer]]
