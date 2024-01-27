from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.base import BaseModel
from youtubei.models.response import Response, ResponseContext
from youtubei.renderers.guide import GuideSectionRenderer, GuideSigninPromoRenderer
from youtubei.renderers.pivot import PivotBarRenderer
from youtubei.types import Dynamic

GuideItem: TypeAlias = Dynamic[PivotBarRenderer]


class GlobalConfigGroup(BaseModel):
    serialized_cold_config_group: str
    serialized_hot_config_group: str
    hot_hash_data: str
    cold_hash_data: str


class IosMusicResponseContext(ResponseContext):
    global_config_group: GlobalConfigGroup


class IosMusicResponse(Response):
    response_context: IosMusicResponseContext


class IosMusicGuideResponse(IosMusicResponse):
    items: Sequence[GuideItem]
