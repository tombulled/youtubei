from typing import Sequence, Union
from typing_extensions import TypeAlias
from youtubei.models.response import Response, ResponseContext
from youtubei.renderers.guide import GuideSectionRenderer, GuideSigninPromoRenderer
from youtubei.types import Renderer

GuideSection: TypeAlias = Renderer[GuideSectionRenderer]
GuideSigninPromo: TypeAlias = Renderer[GuideSigninPromoRenderer]

GuideItem: TypeAlias = Union[GuideSection, GuideSigninPromo]


class WebRemixResponseContext(ResponseContext):
    pass


class WebRemixResponse(Response):
    response_context: WebRemixResponseContext


class WebRemixGuideResponse(WebRemixResponse):
    items: Sequence[GuideItem]
