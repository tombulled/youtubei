from typing import Any, Sequence

from youtubei._registries import ANDROID_REGISTRY, WEB_REGISTRY
from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("ItemSectionRenderer",)


@WEB_REGISTRY
@ANDROID_REGISTRY
class ItemSectionRenderer(BaseRenderer):
    contents: Sequence[Dynamic[Any]]  # Observed: WatchBreakRenderer
