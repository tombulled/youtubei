from typing import Final

from .types import MutableRegistryMapping

__all__ = ("CONTEXT_KEY_REGISTRY", "DEFAULT_REGISTRY")

CONTEXT_KEY_REGISTRY: Final[str] = "registry"
DEFAULT_REGISTRY: MutableRegistryMapping = {}
