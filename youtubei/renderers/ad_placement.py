from youtubei.models.logging import AdSlotLoggingData
from youtubei.models.other import HasAdPlacementConfig
from youtubei.parse import Dynamic

from ._base import BaseRenderer


class AdPlacementRenderer(BaseRenderer):
    config: HasAdPlacementConfig
    renderer: Dynamic  # ClientForecastingAdRenderer
    ad_slot_logging_data: AdSlotLoggingData
