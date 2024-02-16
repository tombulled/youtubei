from youtubei._registries import WEB_REGISTRY
from youtubei.models.other import Icon
from youtubei.enums import BadgeStyleType

from ._base import BaseRenderer


@WEB_REGISTRY
class MetadataBadgeRenderer(BaseRenderer):
    icon: Icon
    style: BadgeStyleType
    label: str
