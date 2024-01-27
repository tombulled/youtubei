from typing import Sequence

from youtubei.renderers.item_section import ItemSectionRenderer
from youtubei.types import Dynamic

from ._base import BaseRenderer


class SectionListRenderer(BaseRenderer):
    contents: Sequence[Dynamic[ItemSectionRenderer]]
