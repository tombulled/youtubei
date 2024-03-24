from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.text import Text
from youtubei.parse.validated_types import Dynamic

from ._base import BaseRenderer
from .button import ButtonRenderer

__all__ = ("ModalWithTitleAndButtonRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class ModalWithTitleAndButtonRenderer(BaseRenderer):
    title: Text  # Observed: SimpleText, ComplexText
    content: Text  # Observed: SimpleText, ComplexText
    button: Dynamic[ButtonRenderer]
