from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.text import ComplexText

from ._base import BaseRenderer


@ANDROID_REGISTRY
@IOS_REGISTRY
class LugashFooterRenderer(BaseRenderer):
    title: ComplexText
