from typing import Sequence

from youtubei._registries import WEB_REGISTRY
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.hotkey_dialog_section import HotkeyDialogSectionRenderer

from ._base import BaseRenderer

__all__ = ("HotkeyDialogRenderer",)


@WEB_REGISTRY
class HotkeyDialogRenderer(BaseRenderer):
    title: ComplexText
    sections: Sequence[Dynamic[HotkeyDialogSectionRenderer]]
    dismiss_button: Dynamic[ButtonRenderer]
