from typing import Union
from typing_extensions import TypeAlias

from youtubei.models.text import ComplexText, SimpleText

Text: TypeAlias = Union[ComplexText, SimpleText]
