from youtubei._registries import IOS_REGISTRY
from youtubei.models.text import ComplexText

from ._base import BaseRenderer

from youtubei._registries import ANDROID_REGISTRY

@ANDROID_REGISTRY
@IOS_REGISTRY
class LugashFooterRenderer(BaseRenderer):
    title: ComplexText
