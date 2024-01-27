from typing import Sequence

from youtubei.renderers.watch_break import WatchBreakRenderer
from youtubei.types import Dynamic

from ._base import BaseRenderer


class ItemSectionRenderer(BaseRenderer):
    contents: Sequence[Dynamic[WatchBreakRenderer]]
