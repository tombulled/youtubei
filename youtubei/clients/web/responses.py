from typing import Optional, Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models._base import BaseModel
from youtubei.models.response import Response, ResponseContext
from youtubei.parse import Dynamic
from youtubei.renderers.desktop_topbar import DesktopTopbarRenderer
from youtubei.renderers.guide_section import GuideSectionRenderer
from youtubei.renderers.guide_signin_promo import GuideSigninPromoRenderer
from youtubei.renderers.microformat_data import MicroformatDataRenderer
from youtubei.renderers.playlist_header import PlaylistHeaderRenderer
from youtubei.renderers.playlist_metadata import PlaylistMetadataRenderer
from youtubei.renderers.playlist_sidebar import PlaylistSidebarRenderer
from youtubei.renderers.two_column_browse_results import TwoColumnBrowseResultsRenderer

__all__ = (
    "MainAppWebResponseContext",
    "WebResponseContextExtensionData",
    "WebResponseContext",
    "WebResponse",
    "WebGuideResponse",
    "WebBrowseResponse",
)

GuideSection: TypeAlias = Dynamic[GuideSectionRenderer]
GuideSigninPromo: TypeAlias = Dynamic[GuideSigninPromoRenderer]

GuideItem: TypeAlias = Union[GuideSection, GuideSigninPromo]


class MainAppWebResponseContext(BaseModel):
    logged_out: bool
    tracking_param: str


class WebResponseContextExtensionData(BaseModel):
    has_decorated: bool


class WebResponseContext(ResponseContext):
    main_app_web_response_context: MainAppWebResponseContext
    web_response_context_extension_data: WebResponseContextExtensionData
    max_age_seconds: Optional[int] = None


class WebResponse(Response):
    response_context: WebResponseContext


class WebGuideResponse(WebResponse):
    items: Sequence[GuideItem]


class WebBrowseResponse(WebResponse):
    contents: Dynamic[TwoColumnBrowseResultsRenderer]
    header: Dynamic[PlaylistHeaderRenderer]
    metadata: Dynamic[PlaylistMetadataRenderer]
    topbar: Dynamic[DesktopTopbarRenderer]
    microformat: Dynamic[MicroformatDataRenderer]
    sidebar: Dynamic[PlaylistSidebarRenderer]
