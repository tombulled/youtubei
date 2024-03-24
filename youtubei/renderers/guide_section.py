from typing import Optional, Sequence

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.guide_entry import GuideEntryRenderer

from ._base import BaseRenderer

__all__ = ("GuideSectionRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class GuideSectionRenderer(BaseRenderer):
    items: Sequence[Dynamic[GuideEntryRenderer]]
    formatted_title: Optional[Text] = None
