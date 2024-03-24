from typing import Optional

from ._base import BaseRenderer

__all__ = ("PlayerStoryboardSpecRenderer",)


class PlayerStoryboardSpecRenderer(BaseRenderer):
    spec: str
    recommended_level: int
    high_resolution_recommended_level: Optional[int] = None
