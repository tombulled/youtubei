from typing import Optional, Sequence
from youtubei.enums import (
    BackgroundPromoStyleType,
    CaptionsInitialState,
    IconType,
    LanguageCode,
    Visibility,
)
from youtubei.models.endpoints import NavigationEndpoint
from youtubei.models.thumbnail import Thumbnails
from youtubei.types import BrowseId, Renderable, TrackingParams

from ._base import BaseModel
from ._types import Text


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
    navigation_endpoint: NavigationEndpoint
    channel_name: str
    subscribe_button: Renderable  # SubscribeButtonRenderer


class Icon(BaseModel):
    icon_type: IconType

class TranslationLanguage(BaseModel):
    languageCode: LanguageCode
    languageName: Text
