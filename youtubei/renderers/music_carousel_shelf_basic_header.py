from youtubei.enums.music import MusicCarouselShelfBasicHeaderStyle
from youtubei.models.accessibility import Accessibility
from youtubei.models.text import ComplexText
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicCarouselShelfBasicHeaderRenderer",)


@WEB_REMIX_REGISTRY
class MusicCarouselShelfBasicHeaderRenderer(BaseRenderer):
    title: ComplexText
    accessibility_data: Accessibility
    header_style: MusicCarouselShelfBasicHeaderStyle
