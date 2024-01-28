from typing import Union

from typing_extensions import TypeAlias

from youtubei.parse import Dynamic
from youtubei.renderers.mobile import MobileTopbarRenderer
from youtubei.renderers.pivot import PivotBarRenderer

GuideItem: TypeAlias = Dynamic[
    Union[
        PivotBarRenderer,
        MobileTopbarRenderer,
    ]
]
