from typing import Optional

from .base import BaseModel


class AccessibilityData(BaseModel):
    label: str


# Note: Potentially referred to internally as 'AccessibilityContext'
class Accessibility(BaseModel):
    accessibility_data: Optional[AccessibilityData] = None
    label: Optional[str] = None
