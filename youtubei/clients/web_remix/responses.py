from typing import Mapping, Optional, Sequence

from youtubei.clients.web_remix.models import GlobalConfigGroup
from youtubei.models.response import Response, ResponseContext
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers import (
    MicroformatDataRenderer,
    MusicDetailHeaderRenderer,
    SingleColumnBrowseResultsRenderer,
    TabbedSearchResultsRenderer,
)
from .types import GuideItem

__all__ = (
    "WebRemixResponseContext",
    "WebRemixResponse",
    "WebRemixConfigResponse",
    "WebRemixGuideResponse",
    "WebRemixGetBrowseAlbumDetailPageResponse",
    "WebRemixGetBrowsePlaylistDetailPageResponse",
)


class WebRemixResponseContext(ResponseContext):
    global_config_group: Optional[GlobalConfigGroup] = None
    max_age_seconds: Optional[int] = None


class WebRemixResponse(Response):
    response_context: WebRemixResponseContext


class WebRemixConfigResponse(WebRemixResponse):
    config_data: str
    global_config: Mapping[None, None]  # WARN: only ever observed as a literal {}


class WebRemixGuideResponse(WebRemixResponse):
    items: Sequence[GuideItem]


class WebRemixGetBrowseAlbumDetailPageResponse(WebRemixResponse):
    contents: Dynamic[SingleColumnBrowseResultsRenderer]
    header: Dynamic[MusicDetailHeaderRenderer]
    microformat: Optional[Dynamic[MicroformatDataRenderer]] = None


class WebRemixGetBrowsePlaylistDetailPageResponse(WebRemixResponse):
    contents: Dynamic[SingleColumnBrowseResultsRenderer]
    header: Optional[Dynamic[MusicDetailHeaderRenderer]] = None


class WebRemixGetSearchResponse(WebRemixResponse):
    contents: Dynamic[TabbedSearchResultsRenderer]
