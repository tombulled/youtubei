from typing import Sequence
from youtubei.models.text import ComplexText
from youtubei.renderers.button import ButtonRenderer
from youtubei.types import Dynamic
from ._base import BaseRenderer


class ConfirmDialogRenderer(BaseRenderer):
    title: ComplexText
    dialog_messages: Sequence[ComplexText]
    confirm_button: Dynamic[ButtonRenderer]
    cancel_button: Dynamic[ButtonRenderer]
