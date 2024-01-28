from youtubei.parse import Dynamic
from ._base import BaseRenderer


class SkipAdRenderer(BaseRenderer):
    preskip_renderer: Dynamic  # AdPreviewRenderer
    skippable_renderer: Dynamic  # SkipButtonRenderer
    skip_offset_milliseconds: int
