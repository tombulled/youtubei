from typing import Optional

from ._base import BaseRenderer


class PlayerStoryboardSpecRenderer(BaseRenderer):
    spec: str
    recommended_level: int
    high_resolution_recommended_level: Optional[int] = None
