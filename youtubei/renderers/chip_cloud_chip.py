from typing import Optional

from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import SearchEndpoint
from youtubei.models.other import Icon, Style
from youtubei.models.text import ComplexText
from youtubei.validated_types import DynamicCommand

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("ChipCloudChipRenderer",)


@WEB_REMIX_REGISTRY
class ChipCloudChipRenderer(BaseRenderer):
    style: Style
    text: Optional[ComplexText] = None
    icon: Optional[Icon] = None
    navigation_endpoint: DynamicCommand[SearchEndpoint]
    accessibility_data: Accessibility
    is_selected: bool
    unique_id: Optional[str] = None
