from typing import Sequence, Union
from typing_extensions import TypeAlias
from youtubei.models import BaseModel
from youtubei.web.models import WebResponseContext
from youtubei.web.renderers import GuideSectionRenderer, GuideSigninPromoRenderer
from youtubei.web.types import WebRenderer

GuideSection: TypeAlias = WebRenderer[GuideSectionRenderer]
GuideSigninPromo: TypeAlias = WebRenderer[GuideSigninPromoRenderer]

GuideItem: TypeAlias = Union[GuideSection, GuideSigninPromo]


class WebGuideResponse(BaseModel):
    response_context: WebResponseContext
    tracking_params: str
    items: Sequence[GuideItem]
