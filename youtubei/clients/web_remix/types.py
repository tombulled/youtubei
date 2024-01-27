from typing import Union

from typing_extensions import TypeAlias

from youtubei.parse import Dynamic
from youtubei.renderers.guide import GuideSectionRenderer, GuideSigninPromoRenderer

GuideItem: TypeAlias = Dynamic[
    Union[
        GuideSectionRenderer,
        GuideSigninPromoRenderer,
    ]
]
