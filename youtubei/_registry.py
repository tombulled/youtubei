from dataclasses import dataclass, field
from typing import Dict, Mapping, MutableMapping, TypeVar

import humps
from typing_extensions import TypeAlias

C = TypeVar("C", bound=type)

# RegistryMapping: TypeAlias = Mapping[str, type]
# MutableRegistry: TypeAlias = MutableMapping[str, type]
# RegistryMapping: TypeAlias = MutableMapping[str, type]


# InnertubeRegistryException
# ClassRegistryException
class RegistryException(Exception):
    pass


def registry_add(registry: MutableMapping[str, type], typ: type, /) -> None:
    key: str = humps.camelize(typ.__name__)

    registry[key] = typ


def registry_get(registry: MutableMapping[str, type], key: str, /) -> None:
    if key not in registry:
        raise RegistryException(f"No entry for {key!r}")

    return registry[key]


class Registry(Dict[str, type]):
    def __call__(self, typ: C, /) -> C:
        self.add(typ)

        return typ


@dataclass
class Registry:
    registry: MutableMapping[str, type] = field(default_factory=dict)

    def __call__(self, typ: C, /) -> C:
        self.add(typ)

        return typ

    def add(self, typ: type, /) -> None:
        key: str = humps.camelize(typ.__name__)

        self.registry[key] = typ

    # def get(self, key: str, /) -> type:
    #     if key not in self.registry:
    #         raise RegistryException(f"No entry for {key!r}")

    #     return self.registry[key]
