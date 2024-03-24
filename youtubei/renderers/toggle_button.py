from typing import Optional

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import ModalEndpoint
from youtubei.models.other import Icon, Size, Style
from youtubei.models.text import ComplexText
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("ToggleButtonRenderer",)


@WEB_REMIX_REGISTRY
@WEB_REGISTRY
class ToggleButtonRenderer(BaseRenderer):
    style: Optional[Style] = None
    size: Optional[Size] = None
    is_toggled: bool
    is_disabled: bool
    default_icon: Icon
    default_text: Optional[ComplexText] = None
    toggled_icon: Icon
    toggled_text: Optional[ComplexText] = None
    default_tooltip: Optional[str] = None
    toggled_tooltip: Optional[str] = None
    toggled_style: Optional[Style] = None
    default_navigation_endpoint: Optional[DynamicCommand[ModalEndpoint]] = None
    accessibility_data: Optional[Accessibility] = None
    toggled_accessibility_data: Optional[Accessibility] = None
