from youtubei.models.endpoints import (
    ChangeEngagementPanelVisibilityAction,
    UrlEndpoint,
    WebviewEndpoint,
)
from youtubei.types import ClickTrackingParams

from .base import BaseModel


class OnTapCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    change_engagement_panel_visibility_action: ChangeEngagementPanelVisibilityAction


class PrivacyCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    url_endpoint: UrlEndpoint


class TosCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    webview_endpoint: WebviewEndpoint
