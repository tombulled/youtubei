from typing import Any, Optional, Sequence

from youtubei import enums
from youtubei.enums import (
    ActiveViewTrafficType,
    AdPlacementKind,
    BackgroundPromoStyleType,
    CaptionsInitialState,
    HeaderType,
    IconType,
    LanguageCode,
    Visibility,
)
from youtubei.enums.action import Action
from youtubei.models.command import Command
from youtubei.models.text import TemplatedText, Text
from youtubei.models.thumbnail import Thumbnails
from youtubei.parse import Dynamic
from youtubei.types import BrowseId, TrackingParams
from youtubei.validated_types import DynamicCommand

from ._base import BaseModel

__all__ = (
    "ActiveViewTracking",
    "AdTemplatedCountdown",
    "AudioTrack",
    "BackgroundPromoStyle",
    "InterpreterSafeUrl",
    "BotguardData",
    "CaptionTrack",
    "CardCueRange",
    "CompletionBehaviorDuration",
    "CsiParameter",
    "EditableDetails",
    "Embed",
    "ErrorBehaviorUntilPageOrContainerSelected",
    "FeaturedChannel",
    "AdTimeOffset",
    "AdPlacementConfig",
    "HasAdPlacementConfig",
    "NotificationResponseConfig",
    "HasNotificationResponseConfig",
    "Icon",
    "LinkAlternate",
    "PageOwnerDetails",
    "PingHeader",
    "Ping",
    "Pings",
    "PlaylistEditAction",
    "ShareData",
    "SodarExtensionData",
    "Style",
    "Size",
    "TranslationLanguage",
    "VideoDetails",
    "QueueTarget",
    "LikeTarget",
    "LikeButtonTarget",
)


class ActiveViewTracking(BaseModel):
    traffic_type: ActiveViewTrafficType


class AdTemplatedCountdown(BaseModel):
    templated_ad_text: TemplatedText


class AudioTrack(BaseModel):
    caption_track_indices: Sequence[int]
    default_caption_track_index: int
    visibility: Visibility
    has_default_track: bool
    captions_initial_state: CaptionsInitialState


class BackgroundPromoStyle(BaseModel):
    value: BackgroundPromoStyleType


class InterpreterSafeUrl(BaseModel):
    private_do_not_access_or_else_trusted_resource_url_wrapped_value: str


class BotguardData(BaseModel):
    program: str
    interpreter_safe_url: InterpreterSafeUrl
    server_environment: int


class CaptionTrack(BaseModel):
    base_url: str
    name: Text
    vss_id: str
    language_code: str
    is_translatable: bool
    track_name: str
    kind: Optional[str] = None


class CardCueRange(BaseModel):
    start_card_active_ms: str
    end_card_active_ms: str
    teaser_duration_ms: str
    icon_after_teaser_ms: str


class CompletionBehaviorDuration(BaseModel):
    seconds: int


class CsiParameter(BaseModel):
    key: str
    value: str


class EditableDetails(BaseModel):
    can_delete: bool


class Embed(BaseModel):
    iframe_url: str
    width: int
    height: int


class ErrorBehaviorUntilPageOrContainerSelected(BaseModel):
    browse_id: BrowseId


class FeaturedChannel(BaseModel):
    start_time_ms: str
    end_time_ms: str
    watermark: Thumbnails
    tracking_params: TrackingParams
    navigation_endpoint: DynamicCommand[Any]
    channel_name: str
    subscribe_button: Dynamic  # Observed: SubscribeButtonRenderer


class AdTimeOffset(BaseModel):
    offset_start_milliseconds: str
    offset_end_milliseconds: str


class AdPlacementConfig(BaseModel):
    kind: AdPlacementKind
    ad_time_offset: AdTimeOffset
    hide_cue_range_marker: bool


class HasAdPlacementConfig(BaseModel):
    ad_placement_config: AdPlacementConfig


class NotificationResponseConfig(BaseModel):
    reactr_enabled: bool


class HasNotificationResponseConfig(BaseModel):
    notification_response_config: NotificationResponseConfig


class Icon(BaseModel):
    icon_type: IconType


class LinkAlternate(BaseModel):
    href_url: str
    title: Optional[str] = None
    alternate_type: Optional[str] = None


class PageOwnerDetails(BaseModel):
    name: str
    external_channel_id: str
    youtube_profile_url: str


class PingHeader(BaseModel):
    header_type: HeaderType


class Ping(BaseModel):
    base_url: str
    headers: Optional[Sequence[PingHeader]] = None
    offset_milliseconds: Optional[int] = None


class Pings(BaseModel):
    activeViewTracking: ActiveViewTracking

    impression_pings: Sequence[Ping]
    error_pings: Sequence[Ping]
    mute_pings: Sequence[Ping]
    unmute_pings: Sequence[Ping]
    pause_pings: Sequence[Ping]
    rewind_pings: Sequence[Ping]
    resume_pings: Sequence[Ping]
    skip_pings: Sequence[Ping]
    close_pings: Sequence[Ping]
    progress_pings: Sequence[Ping]
    clickthrough_pings: Optional[Sequence[Ping]] = None
    fullscreen_pings: Sequence[Ping]
    active_view_viewable_pings: Sequence[Ping]
    end_fullscreen_pings: Sequence[Ping]
    active_view_measurable_pings: Sequence[Ping]
    abandon_pings: Sequence[Ping]
    active_view_fully_viewable_audible_half_duration_pings: Sequence[Ping]
    start_pings: Optional[Sequence[Ping]] = None
    first_quartile_pings: Optional[Sequence[Ping]] = None
    second_quartile_pings: Optional[Sequence[Ping]] = None
    third_quartile_pings: Optional[Sequence[Ping]] = None
    complete_pings: Sequence[Ping]


class PlaylistEditAction(BaseModel):
    action: Action
    source_playlist_id: str


class ShareData(BaseModel):
    can_share: bool


class SodarExtensionData(BaseModel):
    siub: str
    bgub: str
    scs: str
    bgp: str


class Style(BaseModel):
    style_type: enums.Style


class Size(BaseModel):
    size_type: enums.Size


class TranslationLanguage(BaseModel):
    language_code: LanguageCode
    language_name: Text


class VideoDetails(BaseModel):
    external_video_id: str
    duration_seconds: str
    duration_iso8601: str


class QueueTarget(BaseModel):
    video_id: Optional[str] = None
    playlist_id: Optional[str] = None
    on_empty_queue: DynamicCommand[Any]  # Observed: WatchEndpoint


class LikeTarget(BaseModel):
    playlist_id: str


class LikeButtonTarget(BaseModel):
    video_id: str
