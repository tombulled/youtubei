from typing import Any, Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.lugash_footer import LugashFooterRenderer
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("PrivacyTosFooterRenderer",)


@ANDROID_REGISTRY
@IOS_REGISTRY
class PrivacyTosFooterRenderer(BaseRenderer):
    privacy_title: Text
    tos_title: Text
    privacy_command: DynamicCommand[Any]
    tos_command: DynamicCommand[Any]
    footer: Optional[Dynamic[LugashFooterRenderer]] = None
