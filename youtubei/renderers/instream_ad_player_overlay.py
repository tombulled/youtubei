from typing import Any

from youtubei.models.logging import AdLayoutLoggingData
from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("InstreamAdPlayerOverlayRenderer",)


class InstreamAdPlayerOverlayRenderer(BaseRenderer):
    tracking_params: str
    skip_or_preview_renderer: Dynamic[Any]  # Observed: AdPreviewRenderer
    visit_advertiser_renderer: Dynamic[Any]  # Observed: ButtonRenderer
    ad_badge_renderer: Dynamic[Any]  # Observed: SimpleAdBadgeRenderer
    ad_duration_remaining: Dynamic[Any]  # Observed: AdDurationRemainingRenderer
    ad_info_renderer: Dynamic[Any]  # Observed: AdHoverTextButtonRenderer
    ad_layout_logging_data: AdLayoutLoggingData
    element_id: str
    in_player_slot_id: str
    in_player_layout_id: str
