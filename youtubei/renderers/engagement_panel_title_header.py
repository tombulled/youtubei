from youtubei._registries import ANDROID_REGISTRY
from youtubei.models.text import ComplexText

from ._base import BaseRenderer

__all__ = ("EngagementPanelTitleHeaderRenderer",)


@ANDROID_REGISTRY
class EngagementPanelTitleHeaderRenderer(BaseRenderer):
    title: ComplexText
