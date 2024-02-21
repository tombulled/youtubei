from typing import (
    Any,
    Final,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
)

import pydantic
from pydantic import BaseModel, BeforeValidator
from rich.pretty import pprint as pp
from typing_extensions import Annotated, TypeAlias

CONTEXT_KEY_REGISTRY: Final[str] = "registry"


T = TypeVar("T")

RegistryMapping: TypeAlias = Mapping[str, type]
MutableRegistryMapping: TypeAlias = MutableMapping[str, type]


class RegistryException(Exception):
    pass


REGISTRY: MutableRegistryMapping = {}


def validate_dynamic(
    value: Any,
    validation_info: pydantic.ValidationInfo,
) -> Any:
    registry: RegistryMapping = (validation_info.context or {}).get(
        CONTEXT_KEY_REGISTRY, REGISTRY
    )

    if not isinstance(value, Mapping):
        return value

    key, val = next(iter(value.items()))

    if key not in registry:
        raise RegistryException(f"No entry for key {key!r}")

    cls = registry[key]

    return pydantic.TypeAdapter(cls).validate_python(
        val, context=validation_info.context
    )


def parse(
    data: Mapping[str, Any],
    typ: Type[BaseModel],
    /,
    *,
    registry: Optional[RegistryMapping] = None,
):
    return typ.model_validate(
        data,
        context={
            CONTEXT_KEY_REGISTRY: (registry if registry is not None else REGISTRY),
        },
    )


Dynamic: TypeAlias = Annotated[T, BeforeValidator(validate_dynamic)]


class Person(BaseModel):
    name: str
    age: int


class Dog(BaseModel):
    name: str
    age: int


class Cat(BaseModel):
    name: str
    age: int


registry: Mapping[str, type] = {
    "person": Person,
    "dog": Dog,
    "cat": Cat,
}


class Response(BaseModel):
    father: Dynamic[Person]
    pets: Sequence[Dynamic[Union[Dog, Cat]]]


raw_response = {
    "father": {
        "person": {
            "name": "Tom",
            "age": 25,
        },
    },
    "pets": [
        {
            "dog": {
                "name": "Luna",
                "age": 3,
            },
        },
        {
            "cat": {
                "name": "Pudserella",
                "age": 7,
            },
        },
    ],
}
response: Response = parse(raw_response, Response, registry=registry)

pp(response)
