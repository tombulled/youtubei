from typing import Any, Optional

from youtubei._registries import (
    ANDROID_REGISTRY,
    IOS_REGISTRY,
    WEB_REGISTRY,
    WEB_REMIX_REGISTRY,
)
from youtubei.enums import Size, Style, TargetId
from youtubei.models.accessibility import Accessibility
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("ButtonRenderer",)


@WEB_REGISTRY
@ANDROID_REGISTRY
@IOS_REGISTRY
@WEB_REMIX_REGISTRY
class ButtonRenderer(BaseRenderer):
    service_endpoint: Optional[DynamicCommand[Any]] = None
    navigation_endpoint: Optional[DynamicCommand[Any]] = None
    text: Optional[Text] = None
    is_disabled: Optional[bool] = None
    style: Optional[Style] = None
    size: Optional[Size] = None
    icon: Optional[Icon] = None
    accessibility: Optional[Accessibility] = None
    accessibility_data: Optional[Accessibility] = None
    target_id: Optional[TargetId] = None
    command: Optional[DynamicCommand[Any]] = (
        None  # Observed: HideEngagementPanelEndpoint
    )
    tooltip: Optional[str] = None
