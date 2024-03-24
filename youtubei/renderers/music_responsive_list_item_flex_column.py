from typing import Union

from youtubei.enums.music import MusicResponsiveListItemColumnDisplayPriority
from youtubei.models.text import ComplexText, NoText

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicResponsiveListItemFlexColumnRenderer",)


@WEB_REMIX_REGISTRY
class MusicResponsiveListItemFlexColumnRenderer(BaseRenderer):
    text: Union[ComplexText, NoText]
    display_priority: MusicResponsiveListItemColumnDisplayPriority
