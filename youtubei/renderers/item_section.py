from typing import Sequence

from youtubei._registries import ANDROID_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.watch_break import WatchBreakRenderer

from ._base import BaseRenderer


@ANDROID_REGISTRY
class ItemSectionRenderer(BaseRenderer):
    contents: Sequence[Dynamic[WatchBreakRenderer]]
