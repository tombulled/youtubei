from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY, WEB_REGISTRY
from youtubei.models.other import Icon

from ._base import BaseRenderer


@WEB_REGISTRY
@ANDROID_REGISTRY
@IOS_REGISTRY
class TopbarLogoRenderer(BaseRenderer):
    icon_image: Icon
    override_entity_key: str
