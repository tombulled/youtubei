from typing import Optional

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import NavigationEndpoint, ServiceEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text

from ._base import BaseRenderer


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class GuideEntryRenderer(BaseRenderer):
    icon: Icon
    formatted_title: Text
    accessibility: Accessibility
    navigation_endpoint: Optional[NavigationEndpoint] = None
    is_primary: Optional[bool] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    target_id: Optional[str] = None
