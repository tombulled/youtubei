from typing import Optional

from youtubei.enums import Size, Style, TargetId
from youtubei.models.accessibility import Accessibility
from youtubei.models.commands import Command
from youtubei.models.endpoints import NavigationEndpoint, ServiceEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei._registries import WEB_REMIX_REGISTRY

from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class ButtonRenderer(BaseRenderer):
    service_endpoint: Optional[ServiceEndpoint] = None
    navigation_endpoint: Optional[NavigationEndpoint] = None
    text: Optional[Text] = None
    is_disabled: Optional[bool] = None
    style: Optional[Style] = None
    size: Optional[Size] = None
    icon: Optional[Icon] = None
    accessibility: Optional[Accessibility] = None
    accessibility_data: Optional[Accessibility] = None
    target_id: Optional[TargetId] = None
    command: Optional[Command] = None  # HideEngagementPanelEndpoint
