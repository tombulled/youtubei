from typing import Sequence, Union
from typing_extensions import TypeAlias
from youtubei.models.base import BaseModel


class ComplexTextRun(BaseModel):
    text: str


class ComplexText(BaseModel):
    runs: Sequence[ComplexTextRun]


class SimpleText(BaseModel):
    simple_text: str


Text: TypeAlias = Union[ComplexText, SimpleText]
