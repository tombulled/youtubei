from typing import Optional

from youtubei.models.actions import (
    ChangeEngagementPanelVisibilityAction,
    OpenPopupAction,
)
from youtubei.models.endpoints import (
    BrowseEndpoint,
    HideEngagementPanelEndpoint,
    ReelWatchEndpoint,
    SearchEndpoint,
    ShowEngagementPanelEndpoint,
    SignalServiceEndpoint,
    SignInEndpoint,
    SubscribeEndpoint,
    UnsubscribeEndpoint,
    UrlEndpoint,
    WatchEndpoint,
)
from youtubei.models.metadata import CommandMetadata

from .base import BaseModel


class Command(BaseModel):
    """
    Command's contain either:
        * 1x endpoint
        * 1x action
        * hack=True
    """

    click_tracking_params: str
    command_metadata: Optional[CommandMetadata] = None
    hack: Optional[bool] = None

    # Endpoints
    android_app_endpoint: Optional[AndroidAppEndpoint] = None
    app_store_endpoint: AppStoreEndpoint
    application_help_endpoint: Optional[ApplicationHelpEndpoint] = None
    application_settings_endpoint: Optional[ApplicationSettingsEndpoint] = None
    browse_endpoint: Optional[BrowseEndpoint] = None
    hide_engagement_panel_endpoint: Optional[HideEngagementPanelEndpoint] = None
    ios_application_endpoint: Optional[IosApplicationEndpoint] = None
    reel_watch_endpoint: Optional[ReelWatchEndpoint] = None
    search_endpoint: Optional[SearchEndpoint] = None
    show_engagement_panel_endpoint: Optional[ShowEngagementPanelEndpoint] = None
    sign_in_endpoint: Optional[SignInEndpoint] = None
    signal_service_endpoint: Optional[SignalServiceEndpoint] = None
    subscribe_endpoint: Optional[SubscribeEndpoint] = None
    unsubscribe_endpoint: Optional[UnsubscribeEndpoint] = None
    url_endpoint: Optional[UrlEndpoint] = None
    watch_endpoint: Optional[WatchEndpoint] = None
    webview_endpoint: Optional[WebviewEndpoint] = None
    ypc_get_offline_upsell_endpoint: Optional[YpcGetOfflineUpsellEndpoint] = None

    # Actions
    change_engagement_panel_visibility_action: Optional[
        ChangeEngagementPanelVisibilityAction
    ] = None
    open_popup_action: Optional[OpenPopupAction] = None
