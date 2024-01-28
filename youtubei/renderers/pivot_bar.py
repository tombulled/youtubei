from typing import Sequence

from youtubei._registries import IOS_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.pivot_bar_item import PivotBarItemRenderer

from ._base import BaseRenderer

from youtubei._registries import ANDROID_REGISTRY

@ANDROID_REGISTRY
@IOS_REGISTRY
class PivotBarRenderer(BaseRenderer):
    items: Sequence[Dynamic[PivotBarItemRenderer]]