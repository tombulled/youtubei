from typing import Sequence

from youtubei.models.ad import AdSlotMetadata, FulfillmentContent, SlotTrigger

from ._base import BaseRenderer

__all__ = ("AdSlotRenderer",)


class AdSlotRenderer(BaseRenderer):
    ad_slot_metadata: AdSlotMetadata
    fulfillment_content: FulfillmentContent
    slot_entry_trigger: SlotTrigger
    slot_fulfillment_triggers: Sequence[SlotTrigger]
    slot_expiration_triggers: Sequence[SlotTrigger]
