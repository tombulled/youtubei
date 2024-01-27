from typing import Optional, Sequence

from youtubei.models.accessibility import Accessibility
from youtubei.models.base import BaseModel
from youtubei.models.endpoints import NavigationEndpoint, ServiceEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.renderers.button import ButtonRenderer
from youtubei.types import Dynamic
from ._base import BaseRenderer


class GuideEntryRenderer(BaseRenderer):
    icon: Icon
    formatted_title: Text
    accessibility: Accessibility
    navigation_endpoint: Optional[NavigationEndpoint] = None
    is_primary: Optional[bool] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    target_id: Optional[str] = None


class GuideSectionRenderer(BaseRenderer):
    items: Sequence[Dynamic[GuideEntryRenderer]]
    formatted_title: Optional[Text] = None


class GuideSigninPromoRenderer(BaseRenderer):
    action_text: Text
    descriptiveText: Text
    signInButton: Dynamic[ButtonRenderer]
