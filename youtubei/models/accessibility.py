from typing import Optional
from youtubei.models.base import BaseModel


class AccessibilityData(BaseModel):
    label: str


class Accessibility(BaseModel):
    accessibility_data: Optional[AccessibilityData] = None
    label: Optional[str] = None
