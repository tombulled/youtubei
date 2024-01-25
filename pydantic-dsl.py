from typing import Sequence, TypeVar, Union

import humps
import pydantic
from pydantic import BeforeValidator
from rich.pretty import pprint as pp
from typing_extensions import Annotated, TypeAlias

from youtubei.parser import Parser
from youtubei.registry import Registry

T = TypeVar("T")


renderers = Registry()
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
