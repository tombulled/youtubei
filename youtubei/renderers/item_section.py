from typing import Any, Sequence

from youtubei._registries import ANDROID_REGISTRY, WEB_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.watch_break import WatchBreakRenderer

from ._base import BaseRenderer


@WEB_REGISTRY
@ANDROID_REGISTRY
class ItemSectionRenderer(BaseRenderer):
    contents: Sequence[Dynamic[Any]]  # WatchBreakRenderer
