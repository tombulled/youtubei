from typing import Optional

from youtubei.models._base import BaseModel

__all__ = ("BaseRenderer",)


class BaseRenderer(BaseModel):
    tracking_params: Optional[str] = None
