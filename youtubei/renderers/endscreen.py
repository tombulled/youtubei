from typing import Any, Sequence

from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("EndscreenRenderer",)


class EndscreenRenderer(BaseRenderer):
    elements: Sequence[Dynamic[Any]]  # Observed: Sequence[EndscreenElementRenderer]
    start_ms: str
