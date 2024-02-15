from youtubei.models.other import Icon
from youtubei.models.text import ComplexText
from ._base import BaseRenderer

from youtubei._registries import WEB_REMIX_REGISTRY

@WEB_REMIX_REGISTRY
class MenuNavigationItemRenderer(BaseRenderer):
    text: ComplexText
    icon: Icon
