from typing import Sequence

from youtubei.models.reminders import DataReminder
from youtubei.models.response import Response, ResponseContext
from youtubei.parse import Dynamic

from .types import GuideItem

__all__ = (
    "AndroidResponseContext",
    "AndroidResponse",
    "AndroidGuideResponse",
)


class AndroidResponseContext(ResponseContext):
    max_age_seconds: int


class AndroidResponse(Response):
    response_context: AndroidResponseContext


class AndroidGuideResponse(AndroidResponse):
    items: Sequence[GuideItem]
    offline_items: Sequence[GuideItem]
    reminders: Dynamic[DataReminder]
