from typing import Optional

from .base import BaseModel


class Colour(BaseModel):
    red: int
    green: int
    blue: int


class ColourPalette(BaseModel):
    section2_color: Optional[int] = None
    icon_inactive_color: Optional[int] = None
    icon_disabled_color: Optional[int] = None
    icon_inactive_color: Optional[int] = None
