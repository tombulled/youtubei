from typing import Sequence

from ._base import BaseModel

__all__ = ("ComplexTextRun", "ComplexText", "SimpleText")


class ComplexTextRun(BaseModel):
    text: str


class ComplexText(BaseModel):
    runs: Sequence[ComplexTextRun]


class SimpleText(BaseModel):
    simple_text: str
