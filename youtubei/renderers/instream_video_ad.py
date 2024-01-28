from typing import Optional, Sequence

from youtubei.models.endpoints import ClickThroughEndpoint
from youtubei.models.logging import AdLayoutLoggingData
from youtubei.models.other import CsiParameter, Pings, SodarExtensionData
from youtubei.parse import Dynamic

from ._base import BaseRenderer


class InstreamVideoAdRenderer(BaseRenderer):
    tracking_params: str
    layout_id: str
    associated_player_bytes_layout_id: Optional[str] = None
    player_overlay: Optional[Dynamic] = None  # InstreamAdPlayerOverlayRenderer
    skip_offset_milliseconds: Optional[int] = None
    pings: Optional[Pings] = None
    clickthrough_endpoint: Optional[ClickThroughEndpoint] = None
    csi_parameters: Optional[Sequence[CsiParameter]] = None
    player_vars: Optional[str] = None
    element_id: Optional[str] = None
    legacy_info_card_vast_extension: Optional[str] = None
    sodarExtensionData: Optional[SodarExtensionData] = None
    external_video_id: Optional[str] = None
    ad_layout_logging_data: Optional[AdLayoutLoggingData] = None