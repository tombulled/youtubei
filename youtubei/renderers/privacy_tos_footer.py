from typing import Optional

from youtubei._registries import IOS_REGISTRY
from youtubei.models.commands import Command
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.lugash_footer import LugashFooterRenderer

from ._base import BaseRenderer

from youtubei._registries import ANDROID_REGISTRY

@ANDROID_REGISTRY
@IOS_REGISTRY
class PrivacyTosFooterRenderer(BaseRenderer):
    privacy_title: Text
    tos_title: Text
    privacy_command: Command
    tos_command: Command
    footer: Optional[Dynamic[LugashFooterRenderer]] = None
