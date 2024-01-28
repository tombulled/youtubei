from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.reminders import DataReminder
from youtubei.models.response import Response, ResponseContext
from youtubei.renderers.guide import GuideSectionRenderer, GuideSigninPromoRenderer
from youtubei.renderers.mobile_topbar import MobileTopbarRenderer
from youtubei.renderers.pivot import PivotBarRenderer
from youtubei.types import Dynamic

GuideItem: TypeAlias = Dynamic[
    Union[
        PivotBarRenderer,
        MobileTopbarRenderer,
    ]
]


class AndroidResponseContext(ResponseContext):
    max_age_seconds: int


class AndroidResponse(Response):
    response_context: AndroidResponseContext


class AndroidGuideResponse(AndroidResponse):
    items: Sequence[GuideItem]
    offline_items: Sequence[GuideItem]
    reminders: Dynamic[DataReminder]
