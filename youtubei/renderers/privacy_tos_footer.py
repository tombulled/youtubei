from typing import Any, Optional

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.command import Command
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.lugash_footer import LugashFooterRenderer
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


@ANDROID_REGISTRY
@IOS_REGISTRY
class PrivacyTosFooterRenderer(BaseRenderer):
    privacy_title: Text
    tos_title: Text
    privacy_command: DynamicCommand[Any]  # TODO: Type which command(s) expected?
    tos_command: DynamicCommand[Any]  # TODO: Type which command(s) expected?
    footer: Optional[Dynamic[LugashFooterRenderer]] = None
