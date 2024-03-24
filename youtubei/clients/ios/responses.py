from typing import Sequence

from youtubei.models.other import HasNotificationResponseConfig
from youtubei.models.response import Response, ResponseContext

from .types import GuideItem

__all__ = (
    "IosResponseContext",
    "IosResponse",
    "IosGuideResponse",
)


class IosResponseContext(ResponseContext):
    max_age_seconds: int


class IosResponse(Response):
    response_context: IosResponseContext


class IosGuideResponse(IosResponse):
    items: Sequence[GuideItem]
    offline_items: Sequence[GuideItem]
    configs: Sequence[HasNotificationResponseConfig]
