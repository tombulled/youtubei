from typing import Union
from typing_extensions import TypeAlias

from youtubei.models.text import BasicText, ComplexText, SimpleText, TemplatedText

Text: TypeAlias = Union[BasicText, ComplexText, SimpleText, TemplatedText]
