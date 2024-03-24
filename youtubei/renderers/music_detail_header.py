from typing import Optional

from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.cropped_square_thumbnail import CroppedSquareThumbnailRenderer
from youtubei.renderers.menu import MenuRenderer
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
