from typing import Mapping, Optional, Sequence, Union

from youtubei.clients.web_remix.models import GlobalConfigGroup
from youtubei.models.response import Response, ResponseContext
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.single_column_browse_results import SingleColumnBrowseResultsRenderer
from youtubei.renderers.two_column_browse_results import TwoColumnBrowseResultsRenderer

from .types import GuideItem


class WebRemixResponseContext(ResponseContext):
    global_config_group: Optional[GlobalConfigGroup] = None


class WebRemixResponse(Response):
    response_context: WebRemixResponseContext


class WebRemixConfigResponse(WebRemixResponse):
    config_data: str
    global_config: Mapping[None, None]  # Warn: only ever observed as a literal {}


class WebRemixGuideResponse(WebRemixResponse):
    items: Sequence[GuideItem]


class WebRemixBrowseResponse(WebRemixResponse):
    contents: Dynamic[
        Union[
            TwoColumnBrowseResultsRenderer,
            SingleColumnBrowseResultsRenderer,
        ]
    ]
