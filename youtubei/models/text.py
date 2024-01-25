from typing import Optional, Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.accessibility import Accessibility
from youtubei.types import TrackingParams

from .base import BaseModel

"""
Is it worth grouping ComplexText and SimpleText into a single
Text class?

E.g:
class Text(BaseModel):
    runs: Optional[TextRun] = None
    simple_text: Optional[str] = None
"""


class BasicText(BaseModel):
    text: str


class ComplexTextRun(BaseModel):
    text: str


class ComplexText(BaseModel):
    runs: Sequence[ComplexTextRun]


class SimpleText(BaseModel):
    simple_text: str
    accessibility: Optional[Accessibility] = None


class TemplatedText(BaseModel):
    text: str
    is_templated: bool
    tracking_params: TrackingParams


# Text: TypeAlias = Union[BasicText, ComplexText, SimpleText, TemplatedText]
Text: TypeAlias = Union[ComplexText, SimpleText]
