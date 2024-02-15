from youtubei.models.text import ComplexText
from ._base import BaseRenderer
from youtubei._registries import WEB_REMIX_REGISTRY

@WEB_REMIX_REGISTRY
class NotificationTextRenderer(BaseRenderer):
    success_response_text: ComplexText
