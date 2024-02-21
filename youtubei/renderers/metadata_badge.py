from youtubei._registries import WEB_REGISTRY
from youtubei.enums import BadgeStyleType
from youtubei.models.other import Icon

from ._base import BaseRenderer


@WEB_REGISTRY
class MetadataBadgeRenderer(BaseRenderer):
    icon: Icon
    style: BadgeStyleType
    label: str
