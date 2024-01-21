from typing import Optional, Sequence
from youtubei.models import BaseModel
from youtubei.web.enums import (
    ReelPlayerNavigationModel,
    ReelPlayerOverlayStyle,
    Size,
    Style,
)
from youtubei.web.models import SimpleText
from youtubei.web.models.accessibility import Accessibility
from youtubei.web.models.endpoints import NavigationEndpoint, ServiceEndpoint
from youtubei.web.models.other import Icon
from youtubei.web.registry import WEB_REGISTRY
from youtubei.web.types import WebRenderer


@WEB_REGISTRY
class ButtonRenderer(BaseModel):
    tracking_params: str
    # service_endpoint: Optional[ServiceEndpoint] = None
    navigation_endpoint: Optional[NavigationEndpoint] = None
    text: Optional[SimpleText] = None
    is_disabled: Optional[bool] = None
    style: Optional[Style] = None
    size: Optional[Size] = None
    icon: Optional[Icon] = None
    # accessibility: Optional[Accessibility] = None
    # accessibility_data: Optional[Accessibility] = None
    target_id: Optional[str] = None


@WEB_REGISTRY
class GuideEntryRenderer(BaseModel):
    icon: Icon
    tracking_params: str
    formatted_title: SimpleText
    accessibility: Accessibility
    navigation_endpoint: Optional[NavigationEndpoint] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    is_primary: Optional[bool] = None
    target_id: Optional[str] = None


@WEB_REGISTRY
class GuideSectionRenderer(BaseModel):
    tracking_params: str
    items: Sequence[WebRenderer[GuideEntryRenderer]]
    formatted_title: Optional[SimpleText] = None


@WEB_REGISTRY
class GuideSigninPromoRenderer(BaseModel):
    action_text: SimpleText
    descriptiveText: SimpleText
    signInButton: WebRenderer[ButtonRenderer]


@WEB_REGISTRY
class ReelPlayerOverlayRenderer(BaseModel):
    style: ReelPlayerOverlayStyle
    tracking_params: str
    reel_player_navigation_model: ReelPlayerNavigationModel
