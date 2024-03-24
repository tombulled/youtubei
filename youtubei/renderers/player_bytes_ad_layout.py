from typing import Optional, Sequence

from youtubei.models.ad import AdLayoutMetadata, LayoutTrigger
from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("PlayerBytesAdLayoutRenderer",)


class PlayerBytesAdLayoutRenderer(BaseRenderer):
    ad_layout_metadata: AdLayoutMetadata
    rendering_content: Dynamic  # Observed: InstreamVideoAdRenderer, PlayerBytesSequentialLayoutRenderer
    layout_exit_normal_triggers: Optional[Sequence[LayoutTrigger]] = None
    layout_exit_skip_triggers: Optional[Sequence[LayoutTrigger]] = None
    layout_exit_mute_triggers: Optional[Sequence[LayoutTrigger]] = None
