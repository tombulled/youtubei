from youtubei.models.accessibility import Accessibility
from youtubei.models.other import Icon
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicInlineBadgeRenderer",)


@WEB_REMIX_REGISTRY
class MusicInlineBadgeRenderer(BaseRenderer):
    icon: Icon
    accessibility_data: Accessibility
