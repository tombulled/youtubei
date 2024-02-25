from typing import Mapping, Optional, Sequence, Union

from youtubei.clients.web_remix.models import GlobalConfigGroup
from youtubei.models.response import Response, ResponseContext
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.microformat_data import MicroformatDataRenderer
from youtubei.renderers.music_detail_header import MusicDetailHeaderRenderer
from youtubei.renderers.music_thumbnail import MusicThumbnailRenderer
from youtubei.renderers.single_column_browse_results import SingleColumnBrowseResultsRenderer
from youtubei.renderers.two_column_browse_results import TwoColumnBrowseResultsRenderer

from .types import GuideItem


class WebRemixResponseContext(ResponseContext):
    global_config_group: Optional[GlobalConfigGroup] = None
    max_age_seconds: Optional[int] = None


class WebRemixResponse(Response):
    response_context: WebRemixResponseContext
    # max_age_store_seconds: Optional[int] = None


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
    header: Optional[Dynamic[MusicDetailHeaderRenderer]] = None
    microformat: Optional[Dynamic[MicroformatDataRenderer]] = None
    # background: Optional[MusicThumbnailRenderer] = None
