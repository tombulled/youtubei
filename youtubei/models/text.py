from typing import Any, Mapping, Optional, Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.accessibility import Accessibility
from youtubei.types import TrackingParams
from youtubei.validated_types import DynamicCommand

from ._base import BaseModel

__all__ = (
    "BasicText",
    "ComplexTextRun",
    "ComplexText",
    "SimpleText",
    "TemplatedText",
    "NoText",
    "AnyText",
    "Text",
)


class BasicText(BaseModel):
    text: str


class ComplexTextRun(BaseModel):
    text: str
    navigation_endpoint: Optional[DynamicCommand[Any]] = None  # Observed: WatchEndpoint

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"


class ComplexText(BaseModel):
    runs: Sequence[ComplexTextRun]
    accessibility: Optional[Accessibility] = None

    def __str__(self) -> str:
        return "".join(run.text for run in self.runs)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"


class SimpleText(BaseModel):
    simple_text: str
    accessibility: Optional[Accessibility] = None

    def __str__(self) -> str:
        return self.simple_text

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"


# Note: Text potentially referred to internally as "FormattedString"
class TemplatedText(BaseModel):
    text: str
    is_templated: bool
    tracking_params: TrackingParams


NoText: TypeAlias = Mapping[None, None]  # Literal: {}
AnyText: TypeAlias = Union[BasicText, ComplexText, SimpleText, TemplatedText]
Text: TypeAlias = Union[ComplexText, SimpleText]
