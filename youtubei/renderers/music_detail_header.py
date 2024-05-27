from typing import Optional, Sequence

from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.cropped_square_thumbnail import CroppedSquareThumbnailRenderer
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.music_inline_badge import MusicInlineBadgeRenderer
from youtubei.renderers.toggle_button import ToggleButtonRenderer

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicDetailHeaderRenderer",)


@WEB_REMIX_REGISTRY
class MusicDetailHeaderRenderer(BaseRenderer):
    title: ComplexText
    subtitle: ComplexText
    menu: Dynamic[MenuRenderer]
    thumbnail: Dynamic[CroppedSquareThumbnailRenderer]
    description: Optional[ComplexText] = None
    more_button: Dynamic[ToggleButtonRenderer]
    second_subtitle: ComplexText
    subtitle_badges: Optional[Sequence[Dynamic[MusicInlineBadgeRenderer]]] = None
