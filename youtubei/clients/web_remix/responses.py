from typing import Mapping, Sequence

from typing_extensions import Never

from youtubei.models.response import Response, ResponseContext

from .types import GuideItem


class WebRemixResponseContext(ResponseContext):
    pass


class WebRemixResponse(Response):
    response_context: WebRemixResponseContext


class WebRemixConfigResponse(WebRemixResponse):
    config_data: str
    global_config: Mapping[Never, Never]


class WebRemixGuideResponse(WebRemixResponse):
    items: Sequence[GuideItem]
