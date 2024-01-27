from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.base import BaseModel
from youtubei.models.response import Response, ResponseContext
from youtubei.renderers.guide import GuideSectionRenderer, GuideSigninPromoRenderer
from youtubei.types import Dynamic

GuideSection: TypeAlias = Dynamic[GuideSectionRenderer]
GuideSigninPromo: TypeAlias = Dynamic[GuideSigninPromoRenderer]

GuideItem: TypeAlias = Union[GuideSection, GuideSigninPromo]


class MainAppWebResponseContext(BaseModel):
    logged_out: bool
    tracking_param: str


class WebResponseContextExtensionData(BaseModel):
    has_decorated: bool


class WebResponseContext(ResponseContext):
    max_age_seconds: int
    main_app_web_response_context: MainAppWebResponseContext
    web_response_context_extension_data: WebResponseContextExtensionData


class WebResponse(Response):
    response_context: WebResponseContext


class WebGuideResponse(WebResponse):
    items: Sequence[GuideItem]
