from typing import Any, Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.other import Icon
from youtubei.models.command import Command
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


@ANDROID_REGISTRY
@IOS_REGISTRY
class CompactLinkRenderer(BaseRenderer):
    icon: Icon
    title: Text
    navigation_endpoint: DynamicCommand[Any] # TODO: Type which commands expected?
    shouldTintIcon: Optional[bool] = None
