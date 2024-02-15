from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from .button import ButtonRenderer
from ._base import BaseRenderer

from youtubei._registries import WEB_REMIX_REGISTRY

@WEB_REMIX_REGISTRY
class ModalWithTitleAndButtonRenderer(BaseRenderer):
    title: ComplexText
    content: ComplexText
    button: Dynamic[ButtonRenderer]
