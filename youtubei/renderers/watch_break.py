from youtubei.enums import WatchBreakType

from youtubei.models.text import ComplexText
from youtubei.renderers.button import ButtonRenderer
from youtubei.types import Dynamic
from ._base import BaseRenderer


class WatchBreakRenderer(BaseRenderer):
    heading: ComplexText
    notice: ComplexText
    primary_button: Dynamic[ButtonRenderer]
    secondary_button: Dynamic[ButtonRenderer]
    watchBreakType: WatchBreakType
