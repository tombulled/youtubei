from typing import Any, Optional, Sequence

import humps
import pydantic
from typing_extensions import Annotated

from .enums import (
    BackgroundPromoStyleType,
    IconType,
    MusicPageType,
    ReelWatchInputType,
    ReelWatchSequenceProvider,
    SignalActionSignal,
    SignalServiceSignal,
    Target,
    WebPageType,
)
from .parse import parse_renderable
from .types import BrowseId, ClickTrackingParams

__all__ = (
    "Accessibility",
    "AccessibilityData",
    "AppStoreEndpoint",
    "ApplicationHelpEndpoint",
    "ApplicationSettingsEndpoint",
    "BackgroundPromoStyle",
    "BrowseEndpoint",
    "BrowseEndpointContextMusicConfig",
    "BrowseEndpointContextSupportedConfigs",
    "CommandMetadata",
    "CompletionBehaviorDuration",
    "ComplexText",
    "ComplexTextRun",
    "ErrorBehaviorUntilPageOrContainerSelected",
    "Icon",
    "IosApplicationEndpoint",
    "IosApplicationFallbackEndpoint",
    "LoggingContext",
    "LoggingContextContext",
    "NavigationEndpoint",
    "PrivacyCommand",
    "ReelWatchEndpoint",
    "SearchEndpoint",
    "SendFeedbackAction",
    "ServiceEndpoint",
    "SignInEndpoint",
    "SignalAction",
    "SignalServiceAction",
    "SignalServiceEndpoint",
    "SimpleText",
    "SkAdParameters",
    "ThemedThumbnail",
    "Thumbnail",
    "ThumbnailMapEntry",
    "Thumbnails",
    "TosCommand",
    "UrlEndpoint",
    "WebCommandMetadata",
    "WebviewEndpoint",
)

Renderable = Annotated[Any, pydantic.BeforeValidator(parse_renderable)]


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra="forbid",
        alias_generator=humps.camelize,
    )


class Accessibility(BaseModel):
    accessibility_data: Optional["AccessibilityData"] = None
    label: Optional[str] = None


class AccessibilityData(BaseModel):
    label: str


class AppStoreEndpoint(BaseModel):
    app_id: str
    sk_ad_parameters: Optional["SkAdParameters"] = None


class ApplicationHelpEndpoint(BaseModel):
    show_feedback: bool


class ApplicationSettingsEndpoint(BaseModel):
    hack: bool


class BackgroundPromoStyle(BaseModel):
    value: BackgroundPromoStyleType


class BrowseEndpoint(BaseModel):
    browse_id: BrowseId
    params: Optional[str] = None
    browse_endpoint_context_supported_configs: Optional[
        "BrowseEndpointContextSupportedConfigs"
    ] = None


class BrowseEndpointContextMusicConfig(BaseModel):
    page_type: MusicPageType


class BrowseEndpointContextSupportedConfigs(BaseModel):
    browse_endpoint_context_music_config: BrowseEndpointContextMusicConfig


class CommandMetadata(BaseModel):
    web_command_metadata: "WebCommandMetadata"


class CompletionBehaviorDuration(BaseModel):
    seconds: int


class ComplexText(BaseModel):
    runs: Sequence["ComplexTextRun"]

    # def join(self) -> str:
    #     return "".join(run for run in self.runs)


class ComplexTextRun(BaseModel):
    text: str


class ErrorBehaviorUntilPageOrContainerSelected(BaseModel):
    browse_id: BrowseId


class Icon(BaseModel):
    icon_type: IconType


class IosApplicationEndpoint(BaseModel):
    external_app_url: str
    fallback_endpoint: "IosApplicationFallbackEndpoint"


class IosApplicationFallbackEndpoint(BaseModel):
    click_tracking_params: ClickTrackingParams
    app_store_endpoint: AppStoreEndpoint


class LoggingContext(BaseModel):
    vss_logging_context: "LoggingContextContext"
    qoe_logging_context: "LoggingContextContext"


class LoggingContextContext(BaseModel):
    serialized_context_data: str


class NavigationEndpoint(BaseModel):
    click_tracking_params: str
    browse_endpoint: Optional[BrowseEndpoint] = None
    sign_in_endpoint: Optional["SignInEndpoint"] = None
    command_metadata: Optional[CommandMetadata] = None
    url_endpoint: Optional["UrlEndpoint"] = None
    search_endpoint: Optional["SearchEndpoint"] = None
    application_settings_endpoint: Optional[ApplicationSettingsEndpoint] = None
    application_help_endpoint: Optional[ApplicationHelpEndpoint] = None
    ios_application_endpoint: Optional[IosApplicationEndpoint] = None


class PrivacyCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    url_endpoint: "UrlEndpoint"


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


class SendFeedbackAction(BaseModel):
    bucket: str

class ServiceEndpoint(BaseModel):
    click_tracking_params: str
    command_metadata: CommandMetadata
    signal_service_endpoint: Optional["SignalServiceEndpoint"] = None
    reel_watch_endpoint: Optional[ReelWatchEndpoint] = None

class SignInEndpoint(BaseModel):
    hack: bool

class SignalAction(BaseModel):
    signal: SignalActionSignal

class SignalServiceAction(BaseModel):
    click_tracking_params: str
    signal_action: Optional[SignalAction] = None
    send_feedback_action: Optional[SendFeedbackAction] = None

class SignalServiceEndpoint(BaseModel):
    signal: SignalServiceSignal
    actions: Sequence[SignalServiceAction]

class SimpleText(BaseModel):
    simple_text: str

class SkAdParameters(BaseModel):
    campaign_token: str

class ThemedThumbnail(BaseModel):
    thumbnail_map: Sequence["ThumbnailMapEntry"]

class Thumbnail(BaseModel):
    url: str
    width: int
    height: int

class ThumbnailMapEntry(BaseModel):
    key: str
    value: "Thumbnails"

class Thumbnails(BaseModel):
    thumbnails: Sequence[Thumbnail]

class TosCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    webview_endpoint: "WebviewEndpoint"

class UrlEndpoint(BaseModel):
    url: str
    target: Target

class WebCommandMetadata(BaseModel):
    url: Optional[str] = None
    web_page_type: Optional[WebPageType] = None
    root_ve: Optional[int] = None
    api_url: Optional[str] = None
    send_post: Optional[bool] = None


class WebviewEndpoint(BaseModel):
    url: str
