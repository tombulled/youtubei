from typing import Optional, Sequence
from youtubei.models.endpoints import SignInEndpoint

from youtubei.models.other import (
    AudioTrack,
    CaptionTrack,
    FeaturedChannel,
    TranslationLanguage,
)
from youtubei.models._types import Text
from youtubei.models.params import GutParams, PlayerAdParams

from .enums import (
    PlaybackMode,
    ReelPlayerNavigationModel,
    ReelPlayerOverlayStyle,
    Size,
    Style,
    SubscribeButtonType,
    TargetId,
)
from .models import (
    Accessibility,
    BackgroundPromoStyle,
    BaseModel,
    CompletionBehaviorDuration,
    ErrorBehaviorUntilPageOrContainerSelected,
    Icon,
    NavigationEndpoint,
    PrivacyCommand,
    Renderable,
    ServiceEndpoint,
    ThemedThumbnail,
    TosCommand,
)
from .registry import renderer
from .types import TrackingParams

__all__ = (
    "BackgroundPromo",
    "Button",
    "CompactLink",
    "GuideEntry",
    "GuideSection",
    "GuideSigninPromo",
    "MobileTopbar",
    "MultiPageMenu",
    "MultiPageMenuSection",
    "MusicImmersiveHeaderRenderer",
    "PivotBar",
    "PivotBarItem",
    "PrivacyTosFooter",
    "ReelPlayerOverlay",
    "SingleColumnBrowseResultsRenderer",
    "TopbarButton",
    "TopbarLogo",
    "TopbarMenuButton",
    "UploadProgressArrow",
)


# TODO: Use me?
# TODO: Suffix render class names with "Renderer"
class _BaseRenderer(BaseModel):
    pass


@renderer
class BackgroundPromo(BaseModel):
    title: Text
    body_text: Text
    tracking_params: str
    cta_button: Renderable  # Button
    style: BackgroundPromoStyle
    themed_thumbnail: ThemedThumbnail


@renderer
class Button(BaseModel):
    tracking_params: str
    service_endpoint: Optional[ServiceEndpoint] = None
    navigation_endpoint: Optional[NavigationEndpoint] = None
    text: Optional[Text] = None
    is_disabled: Optional[bool] = None
    style: Optional[Style] = None
    size: Optional[Size] = None
    icon: Optional[Icon] = None
    accessibility: Optional[Accessibility] = None
    target_id: Optional[TargetId] = None


@renderer
class CompactLink(BaseModel):
    icon: Icon
    title: Text
    navigation_endpoint: NavigationEndpoint
    tracking_params: TrackingParams


@renderer
class ConfirmDialog(BaseModel):
    tracking_params: TrackingParams
    dialog_messages: Sequence[Text]
    confirm_button: Renderable  # Button
    cancel_button: Renderable  # Button
    primary_is_cancel: bool


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
class Miniplayer(BaseModel):
    playback_mode: PlaybackMode


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
class MultiPageMenu(BaseModel):
    sections: Sequence[Renderable]
    tracking_params: TrackingParams
    footer: Renderable


@renderer
class MultiPageMenuSection(BaseModel):
    tracking_params: TrackingParams
    items: Sequence[Renderable]  # Union[BackgroundPromo, CompactLink]


@renderer
class PivotBar(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]  # Sequence[PivotBarItem]


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
class PlayerAnnotationsExpanded(BaseModel):
    featured_channel: FeaturedChannel
    allow_swipe_dismiss: bool
    annotation_id: str


@renderer
class PlayerCaptionsTracklist(BaseModel):
    caption_tracks: Sequence[CaptionTrack]
    audio_tracks: Sequence[AudioTrack]
    translation_languages: Sequence[TranslationLanguage]
    default_audio_track_index: int


@renderer
class PlayerLegacyDesktopWatchAds(BaseModel):
    playerAdParams: PlayerAdParams
    gut_params: GutParams
    show_companion: bool
    show_instream: bool
    use_gut: bool


@renderer
class PrivacyTosFooter(BaseModel):
    privacy_title: Text
    tos_title: Text
    privacy_command: PrivacyCommand
    tos_command: TosCommand


@renderer
class ReelPlayerOverlay(BaseModel):
    style: ReelPlayerOverlayStyle
    tracking_params: str
    reel_player_navigation_model: ReelPlayerNavigationModel


@renderer
class SubscribeButton(BaseModel):
    button_text: Text
    subscribed: bool
    enabled: bool
    type: SubscribeButtonType
    channel_id: str
    show_preferences: bool
    subscribed_button_text: Text
    unsubscribed_button_text: Text
    tracking_params: TrackingParams
    unsubscribe_button_text: Text
    service_endpoints: Sequence[ServiceEndpoint]
    subscribe_accessibility: Accessibility
    unsubscribe_accessibility: Accessibility
    sign_in_endpoint: SignInEndpoint


@renderer
class TopbarButton(BaseModel):
    button_renderer: Renderable  # Button
    new_content_identifier: Sequence[str]


@renderer
class TopbarLogo(BaseModel):
    icon_image: Icon
    tracking_params: str
    override_entity_key: str


@renderer
class TopbarMenuButton(BaseModel):
    icon: Icon
    menu_renderer: Renderable  # MultiPageMenu
    tracking_params: TrackingParams
    target_id: TargetId


@renderer
class UploadProgressArrow(BaseModel):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected
