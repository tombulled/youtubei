from typing import Mapping, MutableMapping

from typing_extensions import TypeAlias

__all__ = ("RegistryMapping", "MutableRegistryMapping")

RegistryMapping: TypeAlias = Mapping[str, type]
MutableRegistryMapping: TypeAlias = MutableMapping[str, type]
