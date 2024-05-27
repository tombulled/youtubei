from typing import Optional
from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.models.endpoints import LikeEndpoint, ModalEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import ComplexText
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("ToggleMenuServiceItemRenderer",)


@WEB_REMIX_REGISTRY
class ToggleMenuServiceItemRenderer(BaseRenderer):
    default_text: ComplexText
    default_icon: Icon
    default_service_endpoint: DynamicCommand[ModalEndpoint]
    toggled_text: ComplexText
    toggled_icon: Icon
    toggled_service_endpoint: Optional[DynamicCommand[LikeEndpoint]] = None
