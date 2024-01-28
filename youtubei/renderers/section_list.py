from typing import Sequence

from youtubei.parse import Dynamic
from youtubei.renderers.item_section import ItemSectionRenderer

from ._base import BaseRenderer

from youtubei._registries import ANDROID_REGISTRY

@ANDROID_REGISTRY
class SectionListRenderer(BaseRenderer):
    contents: Sequence[Dynamic[ItemSectionRenderer]]
