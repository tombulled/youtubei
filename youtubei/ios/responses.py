from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.other import HasNotificationResponseConfig
from youtubei.models.response import Response, ResponseContext
from youtubei.renderers.mobile import MobileTopbarRenderer
from youtubei.renderers.pivot import PivotBarRenderer
from youtubei.types import Dynamic

GuideItem: TypeAlias = Dynamic[
    Union[
        PivotBarRenderer,
        MobileTopbarRenderer,
    ]
]


class IosResponseContext(ResponseContext):
    max_age_seconds: int


class IosResponse(Response):
    response_context: IosResponseContext


class IosGuideResponse(IosResponse):
    items: Sequence[GuideItem]
    offline_items: Sequence[GuideItem]
    configs: Sequence[HasNotificationResponseConfig]
