from dataclasses import dataclass
from typing import Any, Optional, Type

from pydantic import BaseModel

from .constants import CONTEXT_KEY_REGISTRY, DEFAULT_REGISTRY
from .types import RegistryMapping

__all__ = ("parse", "Parser")


def parse(
    obj: Any,
    typ: Type[BaseModel],
    /,
    *,
    registry: Optional[RegistryMapping] = None,
) -> BaseModel:
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

    def parse(self, obj: Any, typ: Type[BaseModel], /) -> BaseModel:
        return parse(obj, typ, registry=self.registry)
