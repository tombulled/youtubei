from youtubei.models.commands import Command
from youtubei.models.text import Text

from ._base import BaseRenderer


class SimpleCardTeaserRenderer(BaseRenderer):
    message: Text
    prominent: bool
    log_visibility_updates: bool
    onTapCommand: Command
