from typing import Annotated, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class Item(BaseModel):
    value: str


class Container(BaseModel, Generic[T]):
    item: T


HappyContainer = Annotated[Container[T], "happy!"]


class Response(BaseModel):
    container: HappyContainer[str]
    # container: HappyContainer[Item]


response = Response(container=Container(item=Item(value="value")))

# my_container: HappyContainer[Item] = Container(item=Item(value="value"))
