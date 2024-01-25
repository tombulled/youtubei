from typing import Optional, Sequence

from youtubei.models.accessibility import Accessibility
from youtubei.models.base import BaseModel
from youtubei.models.endpoints import NavigationEndpoint, ServiceEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.renderers.button import ButtonRenderer
from youtubei.types import Renderer


class GuideEntryRenderer(BaseModel):
    icon: Icon
    tracking_params: str
    formatted_title: Text
    accessibility: Accessibility
    navigation_endpoint: Optional[NavigationEndpoint] = None
    is_primary: Optional[bool] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    target_id: Optional[str] = None


class GuideSectionRenderer(BaseModel):
    tracking_params: str
    items: Sequence[Renderer[GuideEntryRenderer]]
    formatted_title: Optional[Text] = None


class GuideSigninPromoRenderer(BaseModel):
    action_text: Text
    descriptiveText: Text
    signInButton: Renderer[ButtonRenderer]
