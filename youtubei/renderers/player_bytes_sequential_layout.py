from typing import Sequence

from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("PlayerBytesSequentialLayoutRenderer",)


class PlayerBytesSequentialLayoutRenderer(BaseRenderer):
    sequential_layouts: Sequence[
        Dynamic
    ]  # Observed: Sequence[PlayerBytesAdLayoutRenderer]
