from typing import Any, Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY, WEB_REGISTRY
from youtubei.models.other import Icon
from youtubei.models.text import ComplexText
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("TopbarLogoRenderer",)


@WEB_REGISTRY
@ANDROID_REGISTRY
@IOS_REGISTRY
class TopbarLogoRenderer(BaseRenderer):
    icon_image: Icon
    override_entity_key: str
    tooltip_text: Optional[ComplexText] = None
    endpoint: Optional[DynamicCommand[Any]] = None  # Observed: BrowseEndpoint
