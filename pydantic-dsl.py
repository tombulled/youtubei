from dataclasses import dataclass
from typing import Any, Sequence, TypeVar, Union
import humps
import pydantic
from pydantic import BeforeValidator, TypeAdapter
from rich.pretty import pprint as pp
from typing_extensions import TypeAlias, Annotated
from youtubei.registry import Registry

from youtubei.utils import first_entry

T = TypeVar("T")


renderers = Registry()

@dataclass
class Parser:
    registry: Registry

    def parse(self, data: Any, /) -> Any:
        key, val = first_entry(data)

        cls = self.registry.get(key)

        return TypeAdapter(cls).validate_python(val)

parser = Parser(renderers)

Nested: TypeAlias = Annotated[T, BeforeValidator(parser.parse)]


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra="forbid",
        alias_generator=humps.camelize,
    )


@renderers
class PersonRenderer(BaseModel):
    name: str
    age: int


@renderers
class DogRenderer(BaseModel):
    name: str
    age: int


@renderers
class CatRenderer(BaseModel):
    name: str
    age: int


Person: TypeAlias = Nested[PersonRenderer]
Dog: TypeAlias = Nested[DogRenderer]
Cat: TypeAlias = Nested[CatRenderer]
Pet: TypeAlias = Union[Dog, Cat]


class Response(BaseModel):
    person: Person
    pets: Sequence[Pet]


d = {
    "person": {
        "personRenderer": {
            "name": "Tom",
            "age": 25,
        },
    },
    "pets": [
        {
            "dogRenderer": {
                "name": "Luna",
                "age": 3,
            },
        },
        {
            "catRenderer": {
                "name": "Pudserella",
                "age": 7,
            },
        },
        # {
        #     "fishRenderer": {
        #         "name": "Pudserella",
        #         "age": 7,
        #     },
        # },
    ],
}
r = Response.model_validate(d)

pp(r)
