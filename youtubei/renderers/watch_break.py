from youtubei._registries import ANDROID_REGISTRY
from youtubei.enums import WatchBreakType
from youtubei.models.text import ComplexText
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer

from ._base import BaseRenderer

__all__ = ("WatchBreakRenderer",)


@ANDROID_REGISTRY
class WatchBreakRenderer(BaseRenderer):
    heading: ComplexText
    notice: ComplexText
    primary_button: Dynamic[ButtonRenderer]
    secondary_button: Dynamic[ButtonRenderer]
    watchBreakType: WatchBreakType
