from typing import Optional

from youtubei.models._base import BaseModel


class BaseRenderer(BaseModel):
    tracking_params: Optional[str] = None
