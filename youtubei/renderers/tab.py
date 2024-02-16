from youtubei._registries import WEB_REGISTRY
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.section_list import SectionListRenderer

from ._base import BaseRenderer


@WEB_REGISTRY
class TabRenderer(BaseRenderer):
    selected: bool
    content: Dynamic[SectionListRenderer]
