from typing import Optional

from ._base import BaseModel

__all__ = (
    "Colour",
    "ColourPalette",
)


class Colour(BaseModel):
    red: int
    green: int
    blue: int


class ColourPalette(BaseModel):
    section2_color: Optional[int] = None
    icon_disabled_color: Optional[int] = None
    icon_inactive_color: Optional[int] = None
