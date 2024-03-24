from typing import Any, Optional, Union

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import BrowseEndpoint, UrlEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("GuideEntryRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class GuideEntryRenderer(BaseRenderer):
    icon: Icon
    formatted_title: Text
    accessibility: Accessibility
    navigation_endpoint: Optional[
        DynamicCommand[Union[BrowseEndpoint, UrlEndpoint]]
    ] = None
    is_primary: Optional[bool] = None
    service_endpoint: Optional[DynamicCommand[Any]] = None
    target_id: Optional[str] = None
