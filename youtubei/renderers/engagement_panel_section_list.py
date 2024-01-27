from youtubei.renderers.engagement_panel_title_header import (
    EngagementPanelTitleHeaderRenderer,
)
from youtubei.renderers.section_list import SectionListRenderer
from youtubei.types import Dynamic

from ._base import BaseRenderer


class EngagementPanelSectionListRenderer(BaseRenderer):
    panel_identifier: str
    header: Dynamic[EngagementPanelTitleHeaderRenderer]
    content: Dynamic[SectionListRenderer]
