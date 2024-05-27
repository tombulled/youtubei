
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import SearchEndpoint
from youtubei.models.other import Style
from youtubei.models.text import ComplexText
from youtubei.validated_types import DynamicCommand
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("ChipCloudChipRenderer",)


@WEB_REMIX_REGISTRY
class ChipCloudChipRenderer(BaseRenderer):
    style: Style
    text: ComplexText
    navigation_endpoint: DynamicCommand[SearchEndpoint]
    accessibility_data: Accessibility
    is_selected: bool
    unique_id: str
