from typing import Sequence

from youtubei.parse import Dynamic

from ._base import BaseRenderer


class LinearAdSequenceRenderer(BaseRenderer):
    linear_ads: Sequence[Dynamic]  # Sequence[InstreamVideoAdRenderer]
