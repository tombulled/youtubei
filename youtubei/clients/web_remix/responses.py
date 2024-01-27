from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.response import Response, ResponseContext
from youtubei.parse import Dynamic
from youtubei.renderers.guide import GuideSectionRenderer, GuideSigninPromoRenderer

GuideItem: TypeAlias = Dynamic[
    Union[
        GuideSectionRenderer,
        GuideSigninPromoRenderer,
    ]
]


class WebRemixResponseContext(ResponseContext):
    pass


class WebRemixResponse(Response):
    response_context: WebRemixResponseContext


class WebRemixGuideResponse(WebRemixResponse):
    items: Sequence[GuideItem]
