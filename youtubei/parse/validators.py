from typing import Any, Mapping

from pydantic import TypeAdapter, ValidationInfo

from .constants import CONTEXT_KEY_REGISTRY, DEFAULT_REGISTRY
from .exceptions import RegistryException
from .types import RegistryMapping
from .utils import first_entry

__all__ = ("validate_dynamic",)


def validate_dynamic(
    obj: Any,
    validation_info: ValidationInfo,
) -> Any:
    registry: RegistryMapping = (validation_info.context or {}).get(
        CONTEXT_KEY_REGISTRY, DEFAULT_REGISTRY
    )

    if not isinstance(obj, Mapping):
        return obj

    assert len(obj) == 1, obj

    key, value = first_entry(obj)

    if key not in registry:
        raise RegistryException(f"No entry for key {key!r}")

    cls: type = registry[key]

    return TypeAdapter(cls).validate_python(
        value,
        context=validation_info.context,
    )
