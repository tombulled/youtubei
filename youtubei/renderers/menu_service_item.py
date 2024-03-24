from typing import Any, Optional

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.other import Icon
from youtubei.models.text import ComplexText
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("MenuServiceItemRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class MenuServiceItemRenderer(BaseRenderer):
    text: ComplexText
    icon: Icon
    service_endpoint: Optional[DynamicCommand[Any]] = (
        None  # Observed: ShareEntityServiceEndpoint, QueueAddEndpoint
    )
    has_separator: Optional[bool] = None
