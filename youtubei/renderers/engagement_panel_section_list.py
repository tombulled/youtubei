from youtubei._registries import ANDROID_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.engagement_panel_title_header import (
    EngagementPanelTitleHeaderRenderer,
)
from youtubei.renderers.section_list import SectionListRenderer

from ._base import BaseRenderer

__all__ = ("EngagementPanelSectionListRenderer",)


@ANDROID_REGISTRY
class EngagementPanelSectionListRenderer(BaseRenderer):
    panel_identifier: str
    header: Dynamic[EngagementPanelTitleHeaderRenderer]
    content: Dynamic[SectionListRenderer]
