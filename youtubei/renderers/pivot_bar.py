from typing import Sequence

from youtubei._registries import IOS_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.pivot_bar_item import PivotBarItemRenderer

from ._base import BaseRenderer


@IOS_REGISTRY
class PivotBarRenderer(BaseRenderer):
    items: Sequence[Dynamic[PivotBarItemRenderer]]
