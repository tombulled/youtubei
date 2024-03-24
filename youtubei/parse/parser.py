from dataclasses import dataclass
from typing import Any, Optional, Type, TypeVar

from pydantic import BaseModel

from .constants import CONTEXT_KEY_REGISTRY, DEFAULT_REGISTRY
from .types import RegistryMapping

__all__ = ("parse", "Parser")

M = TypeVar("M", bound=BaseModel)


def parse(
    obj: Any,
    typ: Type[M],
    /,
    *,
    registry: Optional[RegistryMapping] = None,
) -> M:
    return typ.model_validate(
        obj,
        context={
            CONTEXT_KEY_REGISTRY: (
                registry if registry is not None else DEFAULT_REGISTRY
            ),
        },
    )


@dataclass
class Parser:
    registry: Optional[RegistryMapping] = None

    def parse(self, obj: Any, typ: Type[M], /) -> M:
        return parse(obj, typ, registry=self.registry)
