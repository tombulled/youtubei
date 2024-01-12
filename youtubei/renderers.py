from typing import Any, Mapping, MutableMapping, Optional, Sequence, TypeVar, Union

import humps
import pydantic
from typing_extensions import Annotated, TypeAlias

from . import utils
from .enums import (
    BackgroundPromoStyleType,
    IconType,
    MusicPageType,
    ReelPlayerNavigationModel,
    ReelPlayerOverlayStyle,
    ReelWatchInputType,
    ReelWatchSequenceProvider,
    SignalActionSignal,
    SignalServiceSignal,
    Size,
    Style,
    Target,
    TargetId,
    WebPageType,
)

DataMap: TypeAlias = Mapping[str, Mapping[str, Any]]
DataSeq: TypeAlias = Sequence[DataMap]
Data: TypeAlias = Union[DataMap, DataSeq]


def parse_renderable(data: Data, /):
    assert utils.is_renderable(data)

    if isinstance(data, Sequence):
        return [parse_renderable(item) for item in data]

    key = next(iter(data))
    value = data[key]

    if key not in RENDERERS:
        raise Exception(f"No renderer available for {key!r}")

    render_cls: type = RENDERERS[key]

    return render_cls.model_validate(value)


BrowseId: TypeAlias = str
TrackingParams: TypeAlias = str
ClickTrackingParams: TypeAlias = str

Renderable = Annotated[Any, pydantic.BeforeValidator(parse_renderable)]


C = TypeVar("C", bound=type)

RENDERERS: MutableMapping[str, type] = {}


def renderer(cls: C) -> C:
    renderer_id: str = humps.camelize(cls.__name__) + "Renderer"

    RENDERERS[renderer_id] = cls

    return cls


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra="forbid",
        alias_generator=humps.camelize,
    )


class ComplexTextRun(BaseModel):
    text: str


class ComplexText(BaseModel):
    runs: Sequence[ComplexTextRun]

    # def join(self) -> str:
    #     return "".join(run for run in self.runs)


class SimpleText(BaseModel):
    simple_text: str


Text: TypeAlias = Union[ComplexText, SimpleText]


class AccessibilityData(BaseModel):
    label: str


class Accessibility(BaseModel):
    accessibility_data: Optional[AccessibilityData] = None
    label: Optional[str] = None


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


class Icon(BaseModel):
    icon_type: IconType


class SignInEndpoint(BaseModel):
    hack: bool


class WebCommandMetadata(BaseModel):
    url: Optional[str] = None
    web_page_type: Optional[WebPageType] = None
    root_ve: Optional[int] = None
    api_url: Optional[str] = None
    send_post: Optional[bool] = None


class CommandMetadata(BaseModel):
    web_command_metadata: WebCommandMetadata


class UrlEndpoint(BaseModel):
    url: str
    target: Target


class SearchEndpoint(BaseModel):
    query: str


class ApplicationSettingsEndpoint(BaseModel):
    hack: bool


class ApplicationHelpEndpoint(BaseModel):
    show_feedback: bool


class SkAdParameters(BaseModel):
    campaign_token: str


class AppStoreEndpoint(BaseModel):
    app_id: str
    sk_ad_parameters: Optional[SkAdParameters] = None


class IosApplicationFallbackEndpoint(BaseModel):
    click_tracking_params: ClickTrackingParams
    app_store_endpoint: AppStoreEndpoint


class IosApplicationEndpoint(BaseModel):
    external_app_url: str
    fallback_endpoint: IosApplicationFallbackEndpoint


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


class SignalAction(BaseModel):
    signal: SignalActionSignal


class SendFeedbackAction(BaseModel):
    bucket: str


class SignalServiceAction(BaseModel):
    click_tracking_params: str
    signal_action: Optional[SignalAction] = None
    send_feedback_action: Optional[SendFeedbackAction] = None


class SignalServiceEndpoint(BaseModel):
    signal: SignalServiceSignal
    actions: Sequence[SignalServiceAction]


class LoggingContextContext(BaseModel):
    serialized_context_data: str


class LoggingContext(BaseModel):
    vss_logging_context: LoggingContextContext
    qoe_logging_context: LoggingContextContext


class ReelWatchEndpoint(BaseModel):
    player_params: str
    overlay: Renderable
    params: str
    sequence_provider: ReelWatchSequenceProvider
    input_type: ReelWatchInputType
    logging_context: LoggingContext
    ustreamer_config: str


class ServiceEndpoint(BaseModel):
    click_tracking_params: str
    command_metadata: CommandMetadata
    signal_service_endpoint: Optional[SignalServiceEndpoint] = None
    reel_watch_endpoint: Optional[ReelWatchEndpoint] = None


@renderer
class Button(BaseModel):
    navigation_endpoint: NavigationEndpoint
    tracking_params: str
    text: Optional[Text] = None
    is_disabled: Optional[bool] = None
    style: Optional[Style] = None
    size: Optional[Size] = None
    icon: Optional[Icon] = None
    accessibility: Optional[Accessibility] = None
    target_id: Optional[TargetId] = None


@renderer
class SingleColumnBrowseResultsRenderer:
    pass


@renderer
class SingleColumnBrowseResultsRenderer:
    pass


@renderer
class MusicImmersiveHeaderRenderer:
    pass


@renderer
class GuideEntry(BaseModel):
    icon: Icon
    tracking_params: str
    formatted_title: Text
    accessibility: Accessibility
    is_primary: Optional[bool] = None
    navigation_endpoint: Optional[NavigationEndpoint] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    target_id: Optional[TargetId] = None


@renderer
class GuideSection(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]
    formatted_title: Optional[Text] = None


@renderer
class GuideSigninPromo(BaseModel):
    action_text: Text
    descriptiveText: Text
    signInButton: Renderable


@renderer
class ReelPlayerOverlay(BaseModel):
    style: ReelPlayerOverlayStyle
    tracking_params: str
    reel_player_navigation_model: ReelPlayerNavigationModel


class CompletionBehaviorDuration(BaseModel):
    seconds: int


class ErrorBehaviorUntilPageOrContainerSelected(BaseModel):
    browse_id: BrowseId


@renderer
class UploadProgressArrow(BaseModel):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected


@renderer
class PivotBarItem(BaseModel):
    pivot_identifier: str
    navigation_endpoint: NavigationEndpoint
    title: Text
    accessibility: Accessibility
    icon: Icon
    tracking_params: str
    target_id: TargetId
    progress_indicator: Optional[Renderable] = None


@renderer
class PivotBar(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]  # Sequence[PivotBarItem]


@renderer
class MobileTopbar(BaseModel):
    placeholder_text: Text
    tracking_params: TrackingParams
    buttons: Sequence[
        Renderable
    ]  # Sequence[Union[TopbarButton, Button, TopbarMenuButton]]
    controls_cast_button: bool
    topbar_logo: Renderable


@renderer
class TopbarButton(BaseModel):
    button_renderer: Renderable  # Button
    new_content_identifier: Sequence[str]


@renderer
class TopbarMenuButton(BaseModel):
    icon: Icon
    menu_renderer: Renderable  # MultiPageMenu
    tracking_params: TrackingParams
    target_id: TargetId


@renderer
class TopbarLogo(BaseModel):
    icon_image: Icon
    tracking_params: str
    override_entity_key: str


class PrivacyCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    url_endpoint: UrlEndpoint


class WebviewEndpoint(BaseModel):
    url: str


class TosCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    webview_endpoint: WebviewEndpoint


@renderer
class PrivacyTosFooter(BaseModel):
    privacy_title: Text
    tos_title: Text
    privacy_command: PrivacyCommand
    tos_command: TosCommand


@renderer
class CompactLink(BaseModel):
    icon: Icon
    title: Text
    navigation_endpoint: NavigationEndpoint
    tracking_params: TrackingParams


@renderer
class MultiPageMenuSection(BaseModel):
    tracking_params: TrackingParams
    items: Sequence[Renderable]  # Union[BackgroundPromo, CompactLink]


@renderer
class MultiPageMenu(BaseModel):
    sections: Sequence[Renderable]
    tracking_params: TrackingParams
    footer: Renderable


class BackgroundPromoStyle(BaseModel):
    value: BackgroundPromoStyleType


class Thumbnail(BaseModel):
    url: str
    width: int
    height: int


class Thumbnails(BaseModel):
    thumbnails: Sequence[Thumbnail]


class ThumbnailMapEntry(BaseModel):
    key: str
    value: Thumbnails


class ThemedThumbnail(BaseModel):
    thumbnail_map: Sequence[ThumbnailMapEntry]


@renderer
class BackgroundPromo(BaseModel):
    title: Text
    body_text: Text
    tracking_params: str
    cta_button: Renderable  # Button
    style: BackgroundPromoStyle
    themed_thumbnail: ThemedThumbnail
