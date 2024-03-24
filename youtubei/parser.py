from abc import ABC
from typing import Any, Optional, Type, TypeVar

from pydantic import BaseModel

from youtubei.parse import Parser, RegistryMapping

__all__ = ("ClientParser",)

M = TypeVar("M", bound=BaseModel)


class ClientParser(ABC):
    _parser: Parser

    def __init__(self, registry: Optional[RegistryMapping] = None) -> None:
        self._parser = Parser(registry)

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"

    def _parse(self, obj: Any, typ: Type[M], /) -> M:
        return self._parser.parse(obj, typ)
