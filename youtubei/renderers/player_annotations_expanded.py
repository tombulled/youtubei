from youtubei.models.other import FeaturedChannel

from ._base import BaseRenderer

__all__ = ("PlayerAnnotationsExpandedRenderer",)


class PlayerAnnotationsExpandedRenderer(BaseRenderer):
    featured_channel: FeaturedChannel
    allow_swipe_dismiss: bool
    annotation_id: str
