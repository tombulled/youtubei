from typing import TypeVar
from typing_extensions import Annotated, TypeAlias

import pydantic

from youtubei.parser import Parser
from youtubei.web.registry import WEB_REGISTRY

T = TypeVar("T")

WebRenderer: TypeAlias = Annotated[
    T, pydantic.BeforeValidator(Parser(WEB_REGISTRY).parse)
]