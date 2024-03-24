from typing import Union

from typing_extensions import TypeAlias

from youtubei.parse import Dynamic
from youtubei.renderers.mobile_topbar import MobileTopbarRenderer
from youtubei.renderers.pivot_bar import PivotBarRenderer

__all__ = ("GuideItem",)

GuideItem: TypeAlias = Dynamic[
    Union[
        PivotBarRenderer,
        MobileTopbarRenderer,
    ]
]
