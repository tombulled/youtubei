from youtubei.enums.music import MusicResponsiveListItemColumnDisplayPriority
from youtubei.models.text import ComplexText
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class MusicResponsiveListItemFlexColumnRenderer(BaseRenderer):
    text: ComplexText
    display_priority: MusicResponsiveListItemColumnDisplayPriority
