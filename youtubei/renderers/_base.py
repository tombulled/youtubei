from typing import Optional

from youtubei.models.base import BaseModel


class BaseRenderer(BaseModel):
    tracking_params: Optional[str] = None
