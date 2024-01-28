from typing import Optional, Sequence

from youtubei._registries import IOS_REGISTRY
from youtubei.enums import TargetId
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.parse import Dynamic

from ._base import BaseRenderer


@IOS_REGISTRY
class PivotBarItemRenderer(BaseRenderer):
    pivot_identifier: str
    navigation_endpoint: NavigationEndpoint
    title: Text
    accessibility: Accessibility
    icon: Icon
    target_id: TargetId
    progress_indicator: Optional[Dynamic] = None


@IOS_REGISTRY
class PivotBarRenderer(BaseRenderer):
    items: Sequence[Dynamic[PivotBarItemRenderer]]
