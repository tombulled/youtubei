from typing import Optional, Sequence

from youtubei.enums import (
    MusicPageType,
    ReelWatchInputType,
    ReelWatchSequenceProvider,
    SignalServiceSignal,
    Target,
)
from youtubei.models.actions import SignalServiceAction
from youtubei.models.metadata import CommandMetadata
from youtubei.models.other import LoggingContext
from youtubei.models.params import SkAdParameters
from youtubei.types import BrowseId, ClickTrackingParams, Renderable

from ._base import BaseModel


class AppStoreEndpoint(BaseModel):
    app_id: str
    sk_ad_parameters: Optional[SkAdParameters] = None


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


class IosApplicationFallbackEndpoint(BaseModel):
    click_tracking_params: ClickTrackingParams
    app_store_endpoint: AppStoreEndpoint


class IosApplicationEndpoint(BaseModel):
    external_app_url: str
    fallback_endpoint: IosApplicationFallbackEndpoint


class ReelWatchEndpoint(BaseModel):
    player_params: str
    overlay: Renderable
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


class ServiceEndpoint(BaseModel):
    click_tracking_params: str
    command_metadata: CommandMetadata
    signal_service_endpoint: Optional[SignalServiceEndpoint] = None
    reel_watch_endpoint: Optional[ReelWatchEndpoint] = None


class SignInEndpoint(BaseModel):
    hack: bool


class UrlEndpoint(BaseModel):
    url: str
    target: Target


class WebviewEndpoint(BaseModel):
    url: str


class NavigationEndpoint(BaseModel):
    click_tracking_params: str
    browse_endpoint: Optional[BrowseEndpoint] = None
    sign_in_endpoint: Optional[SignInEndpoint] = None
    command_metadata: Optional[CommandMetadata] = None
    url_endpoint: Optional[UrlEndpoint] = None
    search_endpoint: Optional[SearchEndpoint] = None
    application_settings_endpoint: Optional[ApplicationSettingsEndpoint] = None
    application_help_endpoint: Optional[ApplicationHelpEndpoint] = None
    ios_application_endpoint: Optional[IosApplicationEndpoint] = None
