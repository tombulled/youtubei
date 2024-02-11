from typing import Any, Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_MUSIC_REGISTRY, IOS_REGISTRY
from youtubei.enums import TargetId
from youtubei.models.accessibility import Accessibility
from youtubei.models.command import Command
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


@IOS_MUSIC_REGISTRY
@ANDROID_REGISTRY
@IOS_REGISTRY
class PivotBarItemRenderer(BaseRenderer):
    pivot_identifier: str
    navigation_endpoint: DynamicCommand[Any] # TODO: Type which commands expected?
    title: Text
    accessibility: Accessibility
    icon: Icon
    target_id: TargetId
    progress_indicator: Optional[Dynamic] = None
