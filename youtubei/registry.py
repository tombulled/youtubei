from dataclasses import dataclass, field
from typing import MutableMapping, TypeVar

import humps

C = TypeVar("C", bound=type)


class RegistryException(Exception):
    pass


@dataclass
class Registry:
    registry: MutableMapping[str, type] = field(default_factory=dict)

    def __call__(self, typ: C, /) -> C:
        self.add(typ)

        return typ

    def add(self, typ: type, /) -> None:
        key: str = humps.camelize(typ.__name__)

        assert key.endswith("Renderer")

        self.registry[key] = typ

    def get(self, key: str, /) -> type:
        if key not in self.registry:
            raise RegistryException(f"No entry for {key!r}")

        return self.registry[key]
