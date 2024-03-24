from typing import Sequence

from youtubei._registries import WEB_REGISTRY
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.hotkey_dialog_section_option import (
    HotkeyDialogSectionOptionRenderer,
)

from ._base import BaseRenderer

__all__ = ("HotkeyDialogSectionRenderer",)


@WEB_REGISTRY
class HotkeyDialogSectionRenderer(BaseRenderer):
    title: ComplexText
    options: Sequence[Dynamic[HotkeyDialogSectionOptionRenderer]]
