from youtubei.enums import BackgroundPromoStyleType, IconType
from youtubei.types import BrowseId
from ._base import BaseModel


class BackgroundPromoStyle(BaseModel):
    value: BackgroundPromoStyleType


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


class SkAdParameters(BaseModel):
    campaign_token: str
