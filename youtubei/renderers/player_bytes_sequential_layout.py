from typing import Sequence

from youtubei.parse import Dynamic

from ._base import BaseRenderer


class PlayerBytesSequentialLayoutRenderer(BaseRenderer):
    sequential_layouts: Sequence[Dynamic]  # Sequence[PlayerBytesAdLayoutRenderer]
