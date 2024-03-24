from typing import Optional

from youtubei._registries import WEB_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.models.text import ComplexText

from ._base import BaseRenderer

__all__ = ("HotkeyDialogSectionOptionRenderer",)


@WEB_REGISTRY
class HotkeyDialogSectionOptionRenderer(BaseRenderer):
    label: ComplexText
    hotkey: str
    hotkey_accessibility_label: Optional[Accessibility] = None
