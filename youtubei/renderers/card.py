from typing import Sequence

from youtubei.models.other import CardCueRange
from youtubei.parse import Dynamic

from ._base import BaseRenderer


class CardRenderer(BaseRenderer):
    teaser: Dynamic  # SimpleCardTeaserRenderer
    cue_ranges: Sequence[CardCueRange]
