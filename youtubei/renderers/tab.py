from typing import Optional

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.section_list import SectionListRenderer

from ._base import BaseRenderer

__all__ = ("TabRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class TabRenderer(BaseRenderer):
    selected: Optional[bool] = None
    content: Dynamic[SectionListRenderer]
    tab_identifier: Optional[str] = None
    title: Optional[str] = None
