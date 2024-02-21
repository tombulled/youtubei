from typing import Optional

from youtubei._registries import WEB_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import ModalEndpoint
from youtubei.models.other import Icon, Size, Style
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


@WEB_REGISTRY
class ToggleButtonRenderer(BaseRenderer):
    style: Style
    size: Size
    is_toggled: bool
    is_disabled: bool
    default_icon: Icon
    toggled_icon: Icon
    default_tooltip: str
    toggled_tooltip: str
    toggled_style: Optional[Style] = None
    default_navigation_endpoint: DynamicCommand[ModalEndpoint]
    accessibility_data: Accessibility
    toggled_accessibility_data: Accessibility
