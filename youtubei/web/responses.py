from typing import Sequence
from youtubei.models._base import BaseModel
from youtubei.models.response_context import ResponseContext
from youtubei.renderers import GuideSectionRenderer


class GuideResponse(BaseModel):
    response_context: ResponseContext
    tracking_params: str
    items: Sequence[GuideSectionRenderer]
