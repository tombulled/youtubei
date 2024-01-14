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


class CaptionTrack(BaseModel):
    base_url: str
    name: Text
    vss_id: str
    language_code: str
    is_translatable: bool
    track_name: str
    kind: Optional[str] = None


class CompletionBehaviorDuration(BaseModel):
    seconds: int


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
