from youtubei._registries import ANDROID_REGISTRY
from youtubei.models.text import ComplexText

from ._base import BaseRenderer


@ANDROID_REGISTRY
class EngagementPanelTitleHeaderRenderer(BaseRenderer):
    title: ComplexText
