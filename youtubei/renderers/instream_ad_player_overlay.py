from youtubei.models.logging import AdLayoutLoggingData
from youtubei.parse import Dynamic
from ._base import BaseRenderer


class InstreamAdPlayerOverlayRenderer(BaseRenderer):
    tracking_params: str
    skip_or_preview_renderer: Dynamic  # AdPreviewRenderer
    visit_advertiser_renderer: Dynamic  # ButtonRenderer
    ad_badge_renderer: Dynamic  # SimpleAdBadgeRenderer
    ad_duration_remaining: Dynamic  # AdDurationRemainingRenderer
    ad_info_renderer: Dynamic  # AdHoverTextButtonRenderer
    ad_layout_logging_data: AdLayoutLoggingData
    element_id: str
    in_player_slot_id: str
    in_player_layout_id: str
