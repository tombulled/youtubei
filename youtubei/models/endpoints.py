from typing import Optional, Sequence

from youtubei.enums import (
    EngagementPanelVisibility,
    MusicPageType,
    ReelWatchInputType,
    ReelWatchSequenceProvider,
    SignalServiceSignal,
    Target,
    TargetId,
)
from youtubei.models.actions import OpenPopupAction, SignalServiceAction
from youtubei.models.contexts import LoggingContext
from youtubei.models.metadata import CommandMetadata
from youtubei.models.params import SkAdParameters
from youtubei.types import BrowseId, ClickTrackingParams, Dynamic

from .base import BaseModel


class AppStoreEndpoint(BaseModel):
    app_id: str
    sk_ad_parameters: Optional[SkAdParameters] = None
    referrer: Optional[str] = None
    android_deep_link: Optional[str] = None
    android_overlay: Optional[bool] = None


class AndroidAppFallbackEndpoint(BaseModel):
    click_tracking_params: ClickTrackingParams
    app_store_endpoint: AppStoreEndpoint


class AndroidAppEndpoint(BaseModel):
    android_package_name: str
    android_class_name: str
    fallback_endpoint: AndroidAppFallbackEndpoint


class ApplicationHelpEndpoint(BaseModel):
    show_feedback: bool


class ApplicationSettingsEndpoint(BaseModel):
    hack: bool


class BrowseEndpointContextMusicConfig(BaseModel):
    page_type: MusicPageType


class BrowseEndpointContextSupportedConfigs(BaseModel):
    browse_endpoint_context_music_config: BrowseEndpointContextMusicConfig


class BrowseEndpoint(BaseModel):
    browse_id: BrowseId
    params: Optional[str] = None
    browse_endpoint_context_supported_configs: Optional[
        BrowseEndpointContextSupportedConfigs
    ] = None


class ChangeEngagementPanelVisibilityAction(BaseModel):
    target_id: TargetId
    visibility: EngagementPanelVisibility


class HideEngagementPanelEndpoint(BaseModel):
    panel_identifier: str


class IosApplicationFallbackEndpoint(BaseModel):
    click_tracking_params: ClickTrackingParams
    app_store_endpoint: AppStoreEndpoint


class IosApplicationEndpoint(BaseModel):
    external_app_url: str
    fallback_endpoint: IosApplicationFallbackEndpoint


class ReelWatchEndpoint(BaseModel):
    player_params: str
    overlay: Dynamic
    params: str
    sequence_provider: ReelWatchSequenceProvider
    input_type: ReelWatchInputType
    logging_context: LoggingContext
    ustreamer_config: str


class SearchEndpoint(BaseModel):
    query: str


class SignalServiceEndpoint(BaseModel):
    signal: SignalServiceSignal
    actions: Sequence[SignalServiceAction]


class SubscribeEndpoint(BaseModel):
    channel_ids: Sequence[str]
    params: str


class UnsubscribeEndpoint(BaseModel):
    channel_ids: Sequence[str]
    params: str


class ServiceEndpoint(BaseModel):
    click_tracking_params: str
    command_metadata: Optional[CommandMetadata] = None
    signal_service_endpoint: Optional[SignalServiceEndpoint] = None
    reel_watch_endpoint: Optional[ReelWatchEndpoint] = None
    subscribe_endpoint: Optional[SubscribeEndpoint] = None
    unsubscribe_endpoint: Optional[UnsubscribeEndpoint] = None
    open_popup_action: Optional[OpenPopupAction] = None


class ShowEngagementPanelEndpoint(BaseModel):
    panel_identifier: str
    engagement_panel: Dynamic  # EngagementPanelSectionListRenderer


class SignInEndpoint(BaseModel):
    click_tracking_params: Optional[str] = None
    command_metadata: Optional[CommandMetadata] = None
    hack: Optional[bool] = None


class UrlEndpoint(BaseModel):
    url: str
    target: Optional[Target] = None


class WatchEndpoint(BaseModel):
    video_id: str
    playlist_id: Optional[str] = None
    logging_context: Optional[LoggingContext] = None


class WebviewEndpoint(BaseModel):
    url: str


class ClickThroughEndpoint(BaseModel):
    click_tracking_params: ClickTrackingParams
    url_endpoint: UrlEndpoint


class YpcGetOfflineUpsellEndpoint(BaseModel):
    params: str


class NavigationEndpoint(BaseModel):
    click_tracking_params: str
    command_metadata: Optional[CommandMetadata] = None
    browse_endpoint: Optional[BrowseEndpoint] = None
    sign_in_endpoint: Optional[SignInEndpoint] = None
    url_endpoint: Optional[UrlEndpoint] = None
    search_endpoint: Optional[SearchEndpoint] = None
    application_settings_endpoint: Optional[ApplicationSettingsEndpoint] = None
    application_help_endpoint: Optional[ApplicationHelpEndpoint] = None
    ios_application_endpoint: Optional[IosApplicationEndpoint] = None
    ypc_get_offline_upsell_endpoint: Optional[YpcGetOfflineUpsellEndpoint] = None
    android_app_endpoint: Optional[AndroidAppEndpoint] = None
    # Unconfirmed endpoints
    watch_endpoint: Optional[WatchEndpoint] = None
