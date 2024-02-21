from typing import Any

from youtubei.models.command import Command
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


class SimpleCardTeaserRenderer(BaseRenderer):
    message: Text
    prominent: bool
    log_visibility_updates: bool
    onTapCommand: DynamicCommand[Any]  # TODO: Type which command(s) expected?
