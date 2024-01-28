from youtubei._registries import IOS_REGISTRY
from youtubei.models.text import ComplexText

from ._base import BaseRenderer


@IOS_REGISTRY
class LugashFooterRenderer(BaseRenderer):
    title: ComplexText
