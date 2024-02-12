from typing import Optional, Sequence

from youtubei.enums import (
    MusicPageType,
    ReelWatchInputType,
    ReelWatchSequenceProvider,
    SignalServiceSignal,
    Target,
)
from youtubei.models.actions import OpenPopupAction, SignalServiceAction
from youtubei.models.contexts import LoggingContext
from youtubei.models.metadata import CommandMetadata
from youtubei.models.params import SkAdParameters
from youtubei.parse import Dynamic
from youtubei.types import BrowseId, ClickTrackingParams

from .base import BaseModel

# class AppStoreEndpoint(BaseModel):
#     app_id: str
#     sk_ad_parameters: Optional[SkAdParameters] = None
#     referrer: Optional[str] = None
#     android_deep_link: Optional[str] = None
#     android_overlay: Optional[bool] = None


# class AndroidAppFallbackEndpoint(BaseModel):
#     click_tracking_params: ClickTrackingParams
#     app_store_endpoint: AppStoreEndpoint


# class AndroidAppEndpoint(BaseModel):
#     android_package_name: str
#     android_class_name: str
#     fallback_endpoint: AndroidAppFallbackEndpoint


# class ApplicationHelpEndpoint(BaseModel):
#     show_feedback: bool


class ApplicationSettingsEndpoint(BaseModel):
    hack: bool


# class BrowseEndpointContextMusicConfig(BaseModel):
#     page_type: MusicPageType


# class BrowseEndpointContextSupportedConfigs(BaseModel):
#     browse_endpoint_context_music_config: BrowseEndpointContextMusicConfig


# class BrowseEndpoint(BaseModel):
#     browse_id: BrowseId
#     params: Optional[str] = None

#     # Note: this looks like it should be Dynamic?
#     browse_endpoint_context_supported_configs: Optional[
#         BrowseEndpointContextSupportedConfigs
#     ] = None


# class HideEngagementPanelEndpoint(BaseModel):
#     panel_identifier: str


# class IosApplicationFallbackEndpoint(BaseModel):
#     click_tracking_params: ClickTrackingParams
#     app_store_endpoint: AppStoreEndpoint


# class IosApplicationEndpoint(BaseModel):
#     external_app_url: str
#     fallback_endpoint: Command  # AppStoreEndpoint


# class ReelWatchEndpoint(BaseModel):
#     player_params: str
#     overlay: Dynamic
#     params: str
#     sequence_provider: ReelWatchSequenceProvider
#     input_type: ReelWatchInputType
#     logging_context: LoggingContext
#     ustreamer_config: str


# class SearchEndpoint(BaseModel):
#     query: str


class SignalServiceEndpoint(BaseModel):
    signal: SignalServiceSignal

    # class SignalServiceAction(BaseModel):
    #     click_tracking_params: str
    #     signal_action: Optional[SignalAction] = None
    #     send_feedback_action: Optional[SendFeedbackAction] = None
    #     open_popup_action: Optional[OpenPopupAction] = None
    actions: Sequence[SignalServiceAction]


class SubscribeEndpoint(BaseModel):
    channel_ids: Sequence[str]
    params: str


class UnsubscribeEndpoint(BaseModel):
    channel_ids: Sequence[str]
    params: str


# class ShowEngagementPanelEndpoint(BaseModel):
#     panel_identifier: str
#     engagement_panel: Dynamic  # EngagementPanelSectionListRenderer


class UrlEndpoint(BaseModel):
    url: str
    target: Optional[Target] = None


class WatchEndpoint(BaseModel):
    video_id: str
    playlist_id: Optional[str] = None
    logging_context: Optional[LoggingContext] = None


# class WebviewEndpoint(BaseModel):
#     url: str


class YpcGetOfflineUpsellEndpoint(BaseModel):
    params: str
