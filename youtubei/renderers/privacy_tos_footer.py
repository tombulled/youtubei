from typing import Optional
from youtubei.models.base import BaseModel

from youtubei.models.commands import PrivacyCommand, TosCommand
from youtubei.models.text import Text
from youtubei.renderers.lugash_footer import LugashFooterRenderer
from youtubei.types import Renderer


class PrivacyTosFooterRenderer(BaseModel):
    privacy_title: Text
    tos_title: Text
    privacy_command: PrivacyCommand
    tos_command: TosCommand
    footer: Optional[Renderer[LugashFooterRenderer]] = None