from typing import Sequence

from typing_extensions import TypeAlias

from youtubei.models._base import BaseModel
from youtubei.models.response import Response, ResponseContext
from youtubei.parse import Dynamic
from youtubei.renderers.pivot_bar import PivotBarRenderer

__all__ = (
    "GlobalConfigGroup",
    "IosMusicResponseContext",
    "IosMusicResponse",
    "IosMusicGuideResponse",
)

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
