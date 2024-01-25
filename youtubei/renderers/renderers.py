from datetime import datetime
from typing import Optional, Sequence

from youtubei.models.ad import (
    AdLayoutMetadata,
    AdSlotMetadata,
    FulfillmentContent,
    LayoutTrigger,
    SlotTrigger,
)
from youtubei.models.commands import OnTapCommand
from youtubei.models.endpoints import ClickThroughEndpoint, SignInEndpoint
from youtubei.models.logging import AdLayoutLoggingData
from youtubei.models.other import (
    AdSlotLoggingData,
    AdTemplatedCountdown,
    AudioTrack,
    BotguardData,
    CaptionTrack,
    CardCueRange,
    CsiParameter,
    Embed,
    FeaturedChannel,
    HasAdPlacementConfig,
    InterpreterSafeUrl,
    LinkAlternate,
    PageOwnerDetails,
    Pings,
    SodarExtensionData,
    TranslationLanguage,
    VideoDetails,
)
from youtubei.models.params import GutParams, PlayerAdParams
from youtubei.models.text import TemplatedText, Text
from youtubei.models.thumbnail import AdThumbnail, Thumbnails

from ..enums import (
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
from ..models import (
    Accessibility,
    BackgroundPromoStyle,
    BaseModel,
    CompletionBehaviorDuration,
    ErrorBehaviorUntilPageOrContainerSelected,
    Icon,
    NavigationEndpoint,
    PrivacyCommand,
    ServiceEndpoint,
    ThemedThumbnail,
    TosCommand,
)
from ..types import Renderer, TrackingParams


class AboutThisAdRenderer(BaseModel):
    url: InterpreterSafeUrl
    tracking_params: TrackingParams


class AdBreakServiceRenderer(BaseModel):
    prefetch_milliseconds: str
    get_ad_break_url: str


class AdDurationRemainingRenderer(BaseModel):
    templated_countdown: AdTemplatedCountdown
    tracking_params: TrackingParams


class AdHoverTextButtonRenderer(BaseModel):
    button: Renderer  # ButtonRenderer
    hover_text: Text  # ComplexText
    tracking_params: TrackingParams


class AdPlacementRenderer(BaseModel):
    config: HasAdPlacementConfig
    renderer: Renderer  # ClientForecastingAdRenderer
    ad_slot_logging_data: AdSlotLoggingData


class AdPreviewRenderer(BaseModel):
    thumbnail: Optional[AdThumbnail] = None
    tracking_params: TrackingParams
    duration_milliseconds: Optional[int] = None
    templated_countdown: Optional[AdTemplatedCountdown] = None
    static_preview: Optional[Text] = None  # TemplatedText


class AdSlotRenderer(BaseModel):
    ad_slot_metadata: AdSlotMetadata
    fulfillment_content: FulfillmentContent
    slot_entry_trigger: SlotTrigger
    slot_fulfillment_triggers: Sequence[SlotTrigger]
    slot_expiration_triggers: Sequence[SlotTrigger]


class AudioOnlyPlayabilityRenderer(BaseModel):
    tracking_params: TrackingParams
    audio_only_availability: FeatureAvailability


class CardRenderer(BaseModel):
    teaser: Renderer  # SimpleCardTeaserRenderer
    cue_ranges: Sequence[CardCueRange]
    tracking_params: TrackingParams


class CardCollectionRenderer(BaseModel):
    cards: Sequence[Renderer]  # CardRenderer
    header_text: Text
    icon: Renderer  # InfoCardIconRenderer
    close_button: Renderer  # InfoCardIconRenderer
    tracking_params: TrackingParams
    allow_teaser_dismiss: bool
    log_icon_visibility_updates: bool


class ClientForecastingAdRenderer(BaseModel):
    pass


class ConfirmDialogRenderer(BaseModel):
    tracking_params: TrackingParams
    dialog_messages: Sequence[Text]
    confirm_button: Renderer  # Button
    cancel_button: Renderer  # Button
    primary_is_cancel: bool


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
        Sequence[Renderer]
    ] = None  # Sequence[ThumbnailOverlayTimeStatusRenderer]
    playlist_length: Optional[Text] = None


class EndscreenRenderer(BaseModel):
    elements: Sequence[Renderer]  # Sequence[EndscreenElementRenderer]
    start_ms: str
    tracking_params: TrackingParams


class InfoCardIconRenderer(BaseModel):
    tracking_params: TrackingParams


class InstreamAdPlayerOverlayRenderer(BaseModel):
    tracking_params: str
    skip_or_preview_renderer: Renderer  # AdPreviewRenderer
    visit_advertiser_renderer: Renderer  # ButtonRenderer
    ad_badge_renderer: Renderer  # SimpleAdBadgeRenderer
    ad_duration_remaining: Renderer  # AdDurationRemainingRenderer
    ad_info_renderer: Renderer  # AdHoverTextButtonRenderer
    ad_layout_logging_data: AdLayoutLoggingData
    element_id: str
    in_player_slot_id: str
    in_player_layout_id: str


class InstreamVideoAdRenderer(BaseModel):
    tracking_params: str
    layout_id: str
    associated_player_bytes_layout_id: Optional[str] = None
    player_overlay: Optional[Renderer] = None  # InstreamAdPlayerOverlayRenderer
    skip_offset_milliseconds: Optional[int] = None
    pings: Optional[Pings] = None
    clickthrough_endpoint: Optional[ClickThroughEndpoint] = None
    csi_parameters: Optional[Sequence[CsiParameter]] = None
    player_vars: Optional[str] = None
    element_id: Optional[str] = None
    legacy_info_card_vast_extension: Optional[str] = None
    sodarExtensionData: Optional[SodarExtensionData] = None
    external_video_id: Optional[str] = None
    ad_layout_logging_data: Optional[AdLayoutLoggingData] = None


class LinearAdSequenceRenderer(BaseModel):
    linear_ads: Sequence[Renderer]  # Sequence[InstreamVideoAdRenderer]


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


class MiniplayerRenderer(BaseModel):
    playback_mode: PlaybackMode


class MultiPageMenuRenderer(BaseModel):
    sections: Sequence[Renderer]
    tracking_params: TrackingParams
    footer: Renderer


class MultiPageMenuSectionRenderer(BaseModel):
    tracking_params: TrackingParams
    items: Sequence[Renderer]  # Union[BackgroundPromo, CompactLink]


class PlayerAnnotationsExpandedRenderer(BaseModel):
    featured_channel: FeaturedChannel
    allow_swipe_dismiss: bool
    annotation_id: str


class PlayerAttestationRenderer(BaseModel):
    challenge: str
    botguard_data: BotguardData


class PlayerBytesAdLayoutRenderer(BaseModel):
    ad_layout_metadata: AdLayoutMetadata
    rendering_content: Renderer  # Union[InstreamVideoAdRenderer, PlayerBytesSequentialLayoutRenderer]
    layout_exit_normal_triggers: Optional[Sequence[LayoutTrigger]] = None
    layout_exit_skip_triggers: Optional[Sequence[LayoutTrigger]] = None
    layout_exit_mute_triggers: Optional[Sequence[LayoutTrigger]] = None


class PlayerBytesSequentialLayoutRenderer(BaseModel):
    sequential_layouts: Sequence[Renderer]  # Sequence[PlayerBytesAdLayoutRenderer]


class PlayerCaptionsTracklistRenderer(BaseModel):
    caption_tracks: Sequence[CaptionTrack]
    audio_tracks: Sequence[AudioTrack]
    translation_languages: Sequence[TranslationLanguage]
    default_audio_track_index: int


class PlayerErrorMessageRenderer(BaseModel):
    reason: Text
    thumbnail: Thumbnails
    icon: Icon


class PlayerLegacyDesktopWatchAdsRenderer(BaseModel):
    playerAdParams: PlayerAdParams
    gut_params: GutParams
    show_companion: bool
    show_instream: bool
    use_gut: bool


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


class PlayerStoryboardSpecRenderer(BaseModel):
    spec: str
    recommended_level: int
    high_resolution_recommended_level: Optional[int] = None


class PrivacyTosFooterRenderer(BaseModel):
    privacy_title: Text
    tos_title: Text
    privacy_command: PrivacyCommand
    tos_command: TosCommand


class SimpleAdBadgeRenderer(BaseModel):
    text: Text  # ComplexText
    navigation_endpoint: Optional[NavigationEndpoint] = None
    tracking_params: TrackingParams
    icon: Optional[Icon] = None
    style: Optional[Style] = None


class SimpleCardTeaserRenderer(BaseModel):
    message: Text
    tracking_params: TrackingParams
    prominent: bool
    log_visibility_updates: bool
    onTapCommand: OnTapCommand


class SkipAdRenderer(BaseModel):
    preskip_renderer: Renderer  # AdPreviewRenderer
    skippable_renderer: Renderer  # SkipButtonRenderer
    tracking_params: TrackingParams
    skip_offset_milliseconds: int


class SkipButtonRenderer(BaseModel):
    message: TemplatedText
    tracking_params: TrackingParams


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


class ThumbnailOverlayTimeStatusRenderer(BaseModel):
    text: Text
    style: ThumbnailOverlayTimeStatusStyle


class UploadProgressArrowRenderer(BaseModel):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected
