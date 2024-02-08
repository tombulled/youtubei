from typing import Annotated, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Container(BaseModel, Generic[T]):
    item: T


HappyContainer = Annotated[Container[T], "happy!"]
# HappyContainer = Container[T]
# HappyStrContainer = Annotated[Container[str], "happy!"]

my_container: HappyContainer[str] # = Container(item="value")
# my_container: HappyStrContainer # = Container(item="value")
