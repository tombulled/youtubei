from typing import Sequence

from youtubei.parse import Dynamic
from ._base import BaseRenderer


class EndscreenRenderer(BaseRenderer):
    elements: Sequence[Dynamic]  # Sequence[EndscreenElementRenderer]
    start_ms: str
