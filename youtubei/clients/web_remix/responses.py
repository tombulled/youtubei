from typing import Sequence

from youtubei.models.response import Response, ResponseContext

from .types import GuideItem


class WebRemixResponseContext(ResponseContext):
    pass


class WebRemixResponse(Response):
    response_context: WebRemixResponseContext


class WebRemixGuideResponse(WebRemixResponse):
    items: Sequence[GuideItem]
