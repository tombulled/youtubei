from youtubei.enums.music import (
    MusicResponsiveListItemColumnDisplayPriority,
    MusicResponsiveListItemFixedColumnSize,
)
from youtubei.models.text import ComplexText

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicResponsiveListItemFixedColumnRenderer",)


@WEB_REMIX_REGISTRY
class MusicResponsiveListItemFixedColumnRenderer(BaseRenderer):
    text: ComplexText
    display_priority: MusicResponsiveListItemColumnDisplayPriority
    size: MusicResponsiveListItemFixedColumnSize
