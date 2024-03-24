from typing import Any, Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY, WEB_REGISTRY
from youtubei.enums import Style, TargetId
from youtubei.models.accessibility import Accessibility
from youtubei.models.other import Icon
from youtubei.parse import Dynamic
from youtubei.renderers.multi_page_menu import MultiPageMenuRenderer
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("TopbarMenuButtonRenderer",)


@WEB_REGISTRY
@ANDROID_REGISTRY
@IOS_REGISTRY
class TopbarMenuButtonRenderer(BaseRenderer):
    icon: Icon
    menu_renderer: Optional[Dynamic[MultiPageMenuRenderer]] = None
    target_id: Optional[TargetId] = None
    menu_request: Optional[DynamicCommand[Any]] = (
        None  # Observed: SignalServiceEndpoint
    )
    accessibility: Optional[Accessibility] = None
    tooltip: Optional[str] = None
    style: Optional[Style] = None
