from typing import Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_MUSIC_REGISTRY, IOS_REGISTRY
from youtubei.enums import TargetId
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.parse import Dynamic

from ._base import BaseRenderer


@IOS_MUSIC_REGISTRY
@ANDROID_REGISTRY
@IOS_REGISTRY
class PivotBarItemRenderer(BaseRenderer):
    pivot_identifier: str
    navigation_endpoint: NavigationEndpoint
    title: Text
    accessibility: Accessibility
    icon: Icon
    target_id: TargetId
    progress_indicator: Optional[Dynamic] = None
