from typing import Any, Optional

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import BrowseEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class GuideEntryRenderer(BaseRenderer):
    icon: Icon
    formatted_title: Text
    accessibility: Accessibility
    navigation_endpoint: Optional[DynamicCommand[BrowseEndpoint]] = None
    is_primary: Optional[bool] = None
    service_endpoint: Optional[DynamicCommand[Any]] = None # TODO: Type which command expected?
    target_id: Optional[str] = None
