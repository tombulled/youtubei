from typing import Optional, Sequence

from youtubei._registries import ANDROID_REGISTRY
from youtubei.models.text import ComplexText
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer

from ._base import BaseRenderer

__all__ = ("ConfirmDialogRenderer",)


@ANDROID_REGISTRY
class ConfirmDialogRenderer(BaseRenderer):
    title: Optional[ComplexText] = None
    dialog_messages: Sequence[ComplexText]
    confirm_button: Dynamic[ButtonRenderer]
    cancel_button: Dynamic[ButtonRenderer]
    primary_is_cancel: Optional[bool] = None
