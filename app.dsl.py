from pydantic import BaseModel
from rich.pretty import pprint

from youtubei.parse import Dynamic, Parser, Registry

registry = Registry()
parser = Parser(registry)


@registry
class Person(BaseModel):
    name: str
    age: int


@registry
class Response(BaseModel):
    father: Dynamic[Person]
    mother: Dynamic[Person]


raw_response = {
    "father": {
        "person": {
            "name": "Max",
            "age": 47,
        },
    },
    "mother": {
        "person": {
            "name": "Jane",
            "age": 51,
        },
    },
}

response = parser.parse(raw_response, Response)

pprint(response, expand_all=True)
