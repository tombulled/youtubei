from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.models.other import Icon
from youtubei.models.text import ComplexText

from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class MenuServiceItemRenderer(BaseRenderer):
    text: ComplexText
    icon: Icon
