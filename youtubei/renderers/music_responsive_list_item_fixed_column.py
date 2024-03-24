from youtubei.enums.music import MusicResponsiveListItemColumnDisplayPriority, MusicResponsiveListItemFixedColumnSize
from youtubei.models.text import ComplexText
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class MusicResponsiveListItemFixedColumnRenderer(BaseRenderer):
    text: ComplexText
    display_priority: MusicResponsiveListItemColumnDisplayPriority
    size: MusicResponsiveListItemFixedColumnSize
