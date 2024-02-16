from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic

from ._base import BaseRenderer
from .button import ButtonRenderer


@WEB_REMIX_REGISTRY
class ModalWithTitleAndButtonRenderer(BaseRenderer):
    title: ComplexText
    content: ComplexText
    button: Dynamic[ButtonRenderer]
