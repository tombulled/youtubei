from typing import Union

from typing_extensions import TypeAlias

from youtubei.parse import Dynamic
from youtubei.renderers.guide_section import GuideSectionRenderer
from youtubei.renderers.guide_signin_promo import GuideSigninPromoRenderer

__all__ = ("GuideItem",)

GuideItem: TypeAlias = Dynamic[
    Union[
        GuideSectionRenderer,
        GuideSigninPromoRenderer,
    ]
]
