from typing import Any, Sequence

from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("LinearAdSequenceRenderer",)


class LinearAdSequenceRenderer(BaseRenderer):
    linear_ads: Sequence[Dynamic[Any]]  # Observed: Sequence[InstreamVideoAdRenderer]
