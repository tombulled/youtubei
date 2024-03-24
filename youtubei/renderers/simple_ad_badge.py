from typing import Any, Optional

from youtubei.enums import Style
from youtubei.models.command import Command
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.types import TrackingParams
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


class SimpleAdBadgeRenderer(BaseRenderer):
    text: Text  # ComplexText
    navigation_endpoint: Optional[
        DynamicCommand[Any]
    ] = None  # TODO: Type which commands expected?
    tracking_params: TrackingParams
    icon: Optional[Icon] = None
    style: Optional[Style] = None
