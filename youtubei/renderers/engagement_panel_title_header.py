from youtubei.models.text import ComplexText

from ._base import BaseRenderer

from youtubei._registries import ANDROID_REGISTRY

@ANDROID_REGISTRY
class EngagementPanelTitleHeaderRenderer(BaseRenderer):
    title: ComplexText
