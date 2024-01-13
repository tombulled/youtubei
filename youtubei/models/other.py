from typing import Optional, Sequence
from youtubei.enums import (
    BackgroundPromoStyleType,
    CaptionsInitialState,
    IconType,
    LanguageCode,
    Visibility,
)
from youtubei.types import BrowseId

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


class Icon(BaseModel):
    icon_type: IconType


class LoggingContextContext(BaseModel):
    serialized_context_data: str


class LoggingContext(BaseModel):
    vss_logging_context: LoggingContextContext
    qoe_logging_context: LoggingContextContext


class TranslationLanguage(BaseModel):
    languageCode: LanguageCode
    languageName: Text
