from typing import Sequence

from youtubei.models.other import CardCueRange
from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("CardRenderer",)


class CardRenderer(BaseRenderer):
    teaser: Dynamic  # Observed: SimpleCardTeaserRenderer
    cue_ranges: Sequence[CardCueRange]
