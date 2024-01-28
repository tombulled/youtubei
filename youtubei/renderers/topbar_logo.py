from youtubei._registries import IOS_REGISTRY
from youtubei.models.other import Icon

from ._base import BaseRenderer

@IOS_REGISTRY
class TopbarLogoRenderer(BaseRenderer):
    icon_image: Icon
    override_entity_key: str
