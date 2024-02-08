from dataclasses import dataclass
from typing import Any, Collection, Mapping, Sequence, Set, Tuple, Type

from pydantic import BaseModel, TypeAdapter, ValidationInfo

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


@dataclass
class ContainerValidator:
    container_cls: Type[BaseModel]
    field: str
    suffixes: Collection[str]

    def __call__(
        self,
        obj: Any,
        validation_info: ValidationInfo,
    ) -> Any:
        print("Validating:", self, obj, validation_info)

        registry: RegistryMapping = (validation_info.context or {}).get(
            CONTEXT_KEY_REGISTRY, DEFAULT_REGISTRY
        )

        if not isinstance(obj, Mapping):
            return obj

        rich_matches: Sequence[Tuple[str, str]] = [
            (key, suffix.lower())
            for key in obj
            for suffix in self.suffixes
            if key.lower().endswith(suffix.lower())
        ]

        assert len(rich_matches) == 1

        rich_key, suffix = rich_matches[0]
        rich_value = obj[rich_key]
        rich_obj = validate_dynamic({rich_key: rich_value}, validation_info)

        new_obj = {key: value for key, value in obj.items() if key != rich_key}

        new_obj[self.field] = rich_obj
        # new_obj[suffix] = rich_obj

        return self.container_cls.model_validate(
            new_obj,
            context=validation_info.context,
        )
