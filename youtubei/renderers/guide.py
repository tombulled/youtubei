from typing import Optional, Sequence

from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import NavigationEndpoint, ServiceEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer

from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class GuideEntryRenderer(BaseRenderer):
    icon: Icon
    formatted_title: Text
    accessibility: Accessibility
    navigation_endpoint: Optional[NavigationEndpoint] = None
    is_primary: Optional[bool] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    target_id: Optional[str] = None


@WEB_REMIX_REGISTRY
class GuideSectionRenderer(BaseRenderer):
    items: Sequence[Dynamic[GuideEntryRenderer]]
    formatted_title: Optional[Text] = None


@WEB_REMIX_REGISTRY
class GuideSigninPromoRenderer(BaseRenderer):
    action_text: Text
    descriptiveText: Text
    signInButton: Dynamic[ButtonRenderer]
