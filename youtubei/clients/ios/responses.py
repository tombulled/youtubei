from typing import Sequence
from .types import GuideItem
from youtubei.models.other import HasNotificationResponseConfig
from youtubei.models.response import Response, ResponseContext


class IosResponseContext(ResponseContext):
    max_age_seconds: int


class IosResponse(Response):
    response_context: IosResponseContext


class IosGuideResponse(IosResponse):
    items: Sequence[GuideItem]
    offline_items: Sequence[GuideItem]
    configs: Sequence[HasNotificationResponseConfig]
