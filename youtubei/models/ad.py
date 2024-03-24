from typing import Any, Optional

from youtubei.enums import LayoutType, SlotTriggerEvent, SlotType
from youtubei.models.logging import AdLayoutLoggingData, AdSlotLoggingData
from youtubei.parse import Dynamic

from ._base import BaseModel

__all__ = (
    "AdSlotMetadata",
    "AdLayoutMetadata",
    "FulfillmentContent",
    "SlotIdTrigger",
    "SlotTrigger",
    "LayoutRequestedTrigger",
    "LayoutTrigger",
)


class AdSlotMetadata(BaseModel):
    slot_id: str
    slot_type: SlotType
    ad_slot_logging_data: AdSlotLoggingData
    trigger_event: Optional[SlotTriggerEvent] = None


class AdLayoutMetadata(BaseModel):
    layout_id: str
    layout_type: LayoutType
    ad_layout_logging_data: AdLayoutLoggingData


class FulfillmentContent(BaseModel):
    fulfilledLayout: Dynamic[Any]  # Observed: PlayerBytesAdLayoutRenderer


class SlotIdTrigger(BaseModel):
    triggering_slot_id: Optional[str] = None


class SlotTrigger(BaseModel):
    id: str
    # One of:
    before_content_video_id_started_trigger: Optional[SlotIdTrigger] = None
    slot_id_entered_trigger: Optional[SlotIdTrigger] = None
    slot_id_exited_trigger: Optional[SlotIdTrigger] = None
    on_new_playback_after_content_video_id_trigger: Optional[SlotIdTrigger] = None


class LayoutRequestedTrigger(BaseModel):
    triggering_layout_id: str


class LayoutTrigger(BaseModel):
    id: str
    # One of:
    on_layout_self_exit_requested_trigger: Optional[LayoutRequestedTrigger] = None
    skip_requested_trigger: Optional[LayoutRequestedTrigger] = None
