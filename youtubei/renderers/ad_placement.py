from typing import Any

from youtubei.models.logging import AdSlotLoggingData
from youtubei.models.other import HasAdPlacementConfig
from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("AdPlacementRenderer",)


class AdPlacementRenderer(BaseRenderer):
    config: HasAdPlacementConfig
    renderer: Dynamic[Any]  # Observed: ClientForecastingAdRenderer
    ad_slot_logging_data: AdSlotLoggingData
