from typing import Any, Optional

from youtubei.enums import Style
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.types import TrackingParams
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("SimpleAdBadgeRenderer",)


class SimpleAdBadgeRenderer(BaseRenderer):
    text: Text  # Observed: ComplexText
    navigation_endpoint: Optional[DynamicCommand[Any]] = None
    tracking_params: TrackingParams
    icon: Optional[Icon] = None
    style: Optional[Style] = None
