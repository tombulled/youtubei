from typing import Sequence

from youtubei.parse import Dynamic
from youtubei.renderers.item_section import ItemSectionRenderer

from ._base import BaseRenderer


class SectionListRenderer(BaseRenderer):
    contents: Sequence[Dynamic[ItemSectionRenderer]]
