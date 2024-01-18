from datetime import datetime
from typing import Optional, Sequence
from youtubei.models.commands import OnTapCommand
from youtubei.models.endpoints import SignInEndpoint
from youtubei.models.logging import AdLayoutLoggingData

from youtubei.models.other import (
    AdSlotLoggingData,
    AudioTrack,
    BotguardData,
    CaptionTrack,
    CardCueRange,
    Embed,
    FeaturedChannel,
    HasAdPlacementConfig,
    LinkAlternate,
    PageOwnerDetails,
    TranslationLanguage,
    VideoDetails,
)
from youtubei.models._types import Text
from youtubei.models.params import GutParams, PlayerAdParams
from youtubei.models.thumbnail import Thumbnails

from .enums import (
    Category,
    CountryCode,
    EndscreenElementStyle,
    FeatureAvailability,
    PlaybackMode,
    ReelPlayerNavigationModel,
    ReelPlayerOverlayStyle,
    Size,
    Style,
    SubscribeButtonType,
    TargetId,
    ThumbnailOverlayTimeStatusStyle,
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
class AdBreakServiceRenderer(BaseModel):
    prefetch_milliseconds: str
    get_ad_break_url: str


@renderer
class AdPlacementRenderer(BaseModel):
    config: HasAdPlacementConfig
    renderer: Renderable  # ClientForecastingAdRenderer
    ad_slot_logging_data: AdSlotLoggingData


@renderer
class AudioOnlyPlayabilityRenderer(BaseModel):
    tracking_params: TrackingParams
    audio_only_availability: FeatureAvailability


@renderer
class BackgroundPromoRenderer(BaseModel):
    title: Text
    body_text: Text
    tracking_params: str
    cta_button: Renderable  # Button
    style: BackgroundPromoStyle
    themed_thumbnail: ThemedThumbnail


@renderer
class ButtonRenderer(BaseModel):
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
class CardRenderer(BaseModel):
    teaser: Renderable  # SimpleCardTeaserRenderer
    cue_ranges: Sequence[CardCueRange]
    tracking_params: TrackingParams


@renderer
class CardCollectionRenderer(BaseModel):
    cards: Sequence[Renderable]  # CardRenderer
    header_text: Text
    icon: Renderable  # InfoCardIconRenderer
    close_button: Renderable  # InfoCardIconRenderer
    tracking_params: TrackingParams
    allow_teaser_dismiss: bool
    log_icon_visibility_updates: bool


@renderer
class ClientForecastingAdRenderer(BaseModel):
    pass


@renderer
class CompactLinkRenderer(BaseModel):
    icon: Icon
    title: Text
    navigation_endpoint: NavigationEndpoint
    tracking_params: TrackingParams


@renderer
class ConfirmDialogRenderer(BaseModel):
    tracking_params: TrackingParams
    dialog_messages: Sequence[Text]
    confirm_button: Renderable  # Button
    cancel_button: Renderable  # Button
    primary_is_cancel: bool


@renderer
class EndscreenElementRenderer(BaseModel):
    style: EndscreenElementStyle
    image: Thumbnails
    left: float
    width: float
    top: float
    aspect_ratio: float
    start_ms: str
    end_ms: str
    title: Text
    metadata: Text
    endpoint: NavigationEndpoint  # Note: guess taken that this was a NaviationEndpoint, as the field name is ambiguous
    tracking_params: TrackingParams
    id: str
    thumbnail_overlays: Optional[
        Sequence[Renderable]
    ] = None  # Sequence[ThumbnailOverlayTimeStatusRenderer]
    playlist_length: Optional[Text] = None


@renderer
class EndscreenRenderer(BaseModel):
    elements: Sequence[Renderable]  # Sequence[EndscreenElementRenderer]
    start_ms: str
    tracking_params: TrackingParams


@renderer
class GuideEntryRenderer(BaseModel):
    icon: Icon
    tracking_params: str
    formatted_title: Text
    accessibility: Accessibility
    is_primary: Optional[bool] = None
    navigation_endpoint: Optional[NavigationEndpoint] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    target_id: Optional[TargetId] = None


@renderer
class GuideSectionRenderer(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]
    formatted_title: Optional[Text] = None


@renderer
class GuideSigninPromoRenderer(BaseModel):
    action_text: Text
    descriptiveText: Text
    signInButton: Renderable


@renderer
class InfoCardIconRenderer(BaseModel):
    tracking_params: TrackingParams

@renderer
class InstreamAdPlayerOverlayRenderer(BaseModel):
    tracking_params: str
    skip_or_preview_renderer: Renderable # AdPreviewRenderer
    visit_advertiser_renderer: Renderable # ButtonRenderer
    ad_badge_renderer: Renderable # SimpleAdBadgeRenderer
    ad_duration_remaining: Renderable # AdDurationRemainingRenderer
    ad_info_renderer: Renderable # AdHoverTextButtonRenderer
    ad_layout_logging_data: AdLayoutLoggingData
    element_id: str
    in_player_slot_id: str
    in_player_layout_id: str



@renderer
class InstreamVideoAdRenderer(BaseModel):
    player_overlay: Renderable  # InstreamAdPlayerOverlayRenderer
    tracking_params: str
    layout_id: str
    associated_player_bytes_layout_id: str


@renderer
class LinearAdSequenceRenderer(BaseModel):
    linear_ads: Sequence[Renderable]  # Sequence[InstreamVideoAdRenderer]


@renderer
class MicroformatDataRenderer(BaseModel):
    url_canonical: str
    title: str
    description: str
    thumbnail: Thumbnails
    site_name: str
    app_name: str
    android_package: str
    ios_app_store_id: str
    ios_app_arguments: str
    og_type: str
    url_applinks_ios: str
    url_applinks_android: str
    url_twitter_ios: str
    url_twitter_android: str
    twitter_card_type: str
    twitter_site_handle: str
    schema_dot_org_type: str
    noindex: bool
    unlisted: bool
    paid: bool
    family_safe: bool
    tags: Sequence[str]
    page_owner_details: PageOwnerDetails
    video_details: VideoDetails
    link_alternates: Sequence[LinkAlternate]
    view_count: str
    publish_date: datetime
    category: Category
    upload_date: datetime
    available_countries: Optional[Sequence[CountryCode]] = None


@renderer
class MiniplayerRenderer(BaseModel):
    playback_mode: PlaybackMode


@renderer
class MobileTopbarRenderer(BaseModel):
    placeholder_text: Text
    tracking_params: TrackingParams
    buttons: Sequence[
        Renderable
    ]  # Sequence[Union[TopbarButton, Button, TopbarMenuButton]]
    controls_cast_button: bool
    topbar_logo: Renderable


@renderer
class MultiPageMenuRenderer(BaseModel):
    sections: Sequence[Renderable]
    tracking_params: TrackingParams
    footer: Renderable


@renderer
class MultiPageMenuSectionRenderer(BaseModel):
    tracking_params: TrackingParams
    items: Sequence[Renderable]  # Union[BackgroundPromo, CompactLink]


@renderer
class PivotBarRenderer(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]  # Sequence[PivotBarItem]


@renderer
class PivotBarItemRenderer(BaseModel):
    pivot_identifier: str
    navigation_endpoint: NavigationEndpoint
    title: Text
    accessibility: Accessibility
    icon: Icon
    tracking_params: str
    target_id: TargetId
    progress_indicator: Optional[Renderable] = None


@renderer
class PlayerAnnotationsExpandedRenderer(BaseModel):
    featured_channel: FeaturedChannel
    allow_swipe_dismiss: bool
    annotation_id: str


@renderer
class PlayerAttestationRenderer(BaseModel):
    challenge: str
    botguard_data: BotguardData


@renderer
class PlayerCaptionsTracklistRenderer(BaseModel):
    caption_tracks: Sequence[CaptionTrack]
    audio_tracks: Sequence[AudioTrack]
    translation_languages: Sequence[TranslationLanguage]
    default_audio_track_index: int


@renderer
class PlayerErrorMessageRenderer(BaseModel):
    reason: Text
    thumbnail: Thumbnails
    icon: Icon


@renderer
class PlayerLegacyDesktopWatchAdsRenderer(BaseModel):
    playerAdParams: PlayerAdParams
    gut_params: GutParams
    show_companion: bool
    show_instream: bool
    use_gut: bool


@renderer
class PlayerMicroformatRenderer(BaseModel):
    thumbnail: Thumbnails
    embed: Embed
    title: Text
    description: Text
    length_seconds: str
    owner_profile_url: str
    external_channel_id: str
    is_family_safe: bool
    available_countries: Sequence[CountryCode]
    is_unlisted: bool
    has_ypc_metadata: bool
    view_count: str
    category: Category
    publish_date: datetime
    owner_channel_name: str
    upload_date: datetime


@renderer
class PlayerStoryboardSpecRenderer(BaseModel):
    spec: str
    recommended_level: int
    high_resolution_recommended_level: Optional[int] = None


@renderer
class PrivacyTosFooterRenderer(BaseModel):
    privacy_title: Text
    tos_title: Text
    privacy_command: PrivacyCommand
    tos_command: TosCommand


@renderer
class ReelPlayerOverlayRenderer(BaseModel):
    style: ReelPlayerOverlayStyle
    tracking_params: str
    reel_player_navigation_model: ReelPlayerNavigationModel


@renderer
class SimpleCardTeaserRenderer(BaseModel):
    message: Text
    tracking_params: TrackingParams
    prominent: bool
    log_visibility_updates: bool
    onTapCommand: OnTapCommand


@renderer
class SubscribeButtonRenderer(BaseModel):
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
class ThumbnailOverlayTimeStatusRenderer(BaseModel):
    text: Text
    style: ThumbnailOverlayTimeStatusStyle


@renderer
class TopbarButtonRenderer(BaseModel):
    button_renderer: Renderable  # Button
    new_content_identifier: Sequence[str]


@renderer
class TopbarLogoRenderer(BaseModel):
    icon_image: Icon
    tracking_params: str
    override_entity_key: str


@renderer
class TopbarMenuButtonRenderer(BaseModel):
    icon: Icon
    menu_renderer: Renderable  # MultiPageMenu
    tracking_params: TrackingParams
    target_id: TargetId


@renderer
class UploadProgressArrowRenderer(BaseModel):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected
