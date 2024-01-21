from typing import Any, Optional, Sequence
from youtubei.models import BaseModel
from youtubei.web.enums import ReelWatchInputType, ReelWatchSequenceProvider, Signal, Target
from youtubei.web.models.actions import SignalServiceAction
from youtubei.web.models.logging import LoggingContext
from youtubei.web.models.metadata import CommandMetadata
from youtubei.web.types import WebRenderer

class BrowseEndpoint(BaseModel):
    browse_id: str
    params: Optional[str] = None
    # browse_endpoint_context_supported_configs: Optional[
    #     BrowseEndpointContextSupportedConfigs
    # ] = None

class ReelWatchEndpoint(BaseModel):
    player_params: str
    overlay: WebRenderer[Any] # ReelPlayerOverlay (cyclic)
    params: str
    sequence_provider: ReelWatchSequenceProvider
    input_type: ReelWatchInputType
    logging_context: LoggingContext
    ustreamer_config: str

class SignalServiceEndpoint(BaseModel):
    signal: Signal
    actions: Sequence[SignalServiceAction]

class SignInEndpoint(BaseModel):
    click_tracking_params: Optional[str] = None
    command_metadata: Optional[CommandMetadata] = None
    hack: Optional[bool] = None


class ServiceEndpoint(BaseModel):
    click_tracking_params: str
    command_metadata: Optional[CommandMetadata] = None
    signal_service_endpoint: Optional[SignalServiceEndpoint] = None
    reel_watch_endpoint: Optional[ReelWatchEndpoint] = None
    # subscribe_endpoint: Optional[SubscribeEndpoint] = None
    # unsubscribe_endpoint: Optional[UnsubscribeEndpoint] = None
    # open_popup_action: Optional[OpenPopupAction] = None


class UrlEndpoint(BaseModel):
    url: str
    target: Target


class NavigationEndpoint(BaseModel):
    click_tracking_params: str
    command_metadata: Optional[CommandMetadata] = None
    browse_endpoint: Optional[BrowseEndpoint] = None
    sign_in_endpoint: Optional[SignInEndpoint] = None
    url_endpoint: Optional[UrlEndpoint] = None
    # search_endpoint: Optional[SearchEndpoint] = None
    # application_settings_endpoint: Optional[ApplicationSettingsEndpoint] = None
    # application_help_endpoint: Optional[ApplicationHelpEndpoint] = None
    # ios_application_endpoint: Optional[IosApplicationEndpoint] = None
    # ypc_get_offline_upsell_endpoint: Optional[YpcGetOfflineUpsellEndpoint] = None
    # # Unconfirmed endpoints
    # watch_endpoint: Optional[WatchEndpoint] = None
