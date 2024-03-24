from typing import Any

from youtubei.models.text import Text
from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("AdHoverTextButtonRenderer",)


class AdHoverTextButtonRenderer(BaseRenderer):
    button: Dynamic[Any]  # Observed: ButtonRenderer
    hover_text: Text  # Observed: ComplexText
