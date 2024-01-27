from typing import Optional

from youtubei.models.commands import Command
from youtubei.models.text import Text
from youtubei.renderers.lugash_footer import LugashFooterRenderer
from youtubei.types import Dynamic

from ._base import BaseRenderer


class PrivacyTosFooterRenderer(BaseRenderer):
    privacy_title: Text
    tos_title: Text
    privacy_command: Command
    tos_command: Command
    footer: Optional[Dynamic[LugashFooterRenderer]] = None
