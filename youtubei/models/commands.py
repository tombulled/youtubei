from typing import Optional

from youtubei.models.endpoints import (
    AppStoreEndpoint,
    ChangeEngagementPanelVisibilityAction,
    HideEngagementPanelEndpoint,
    ShowEngagementPanelEndpoint,
    UrlEndpoint,
    WebviewEndpoint,
)
from youtubei.types import ClickTrackingParams

from .base import BaseModel


class Command(BaseModel):
    click_tracking_params: ClickTrackingParams

    # One of:

    # Endpoints
    app_store_endpoint: AppStoreEndpoint
    hide_engagement_panel_endpoint: Optional[HideEngagementPanelEndpoint] = None
    webview_endpoint: Optional[WebviewEndpoint] = None
    show_engagement_panel_endpoint: Optional[ShowEngagementPanelEndpoint] = None
    url_endpoint: Optional[UrlEndpoint] = None

    # Actions
    change_engagement_panel_visibility_action: Optional[
        ChangeEngagementPanelVisibilityAction
    ] = None
