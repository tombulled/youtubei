from typing import Any, Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("CompactLinkRenderer",)


@ANDROID_REGISTRY
@IOS_REGISTRY
class CompactLinkRenderer(BaseRenderer):
    icon: Icon
    title: Text
    navigation_endpoint: DynamicCommand[Any]
    should_tint_icon: Optional[bool] = None
