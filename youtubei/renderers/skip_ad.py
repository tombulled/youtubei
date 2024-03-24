from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("SkipAdRenderer",)


class SkipAdRenderer(BaseRenderer):
    preskip_renderer: Dynamic  # Observed: AdPreviewRenderer
    skippable_renderer: Dynamic  # Observed: SkipButtonRenderer
    skip_offset_milliseconds: int
