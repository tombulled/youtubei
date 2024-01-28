from typing import Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text

from ._base import BaseRenderer


@ANDROID_REGISTRY
@IOS_REGISTRY
class CompactLinkRenderer(BaseRenderer):
    icon: Icon
    title: Text
    navigation_endpoint: NavigationEndpoint
    shouldTintIcon: Optional[bool] = None
