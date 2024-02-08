from typing import Generic, Sequence, TypeVar
from typing_extensions import Annotated
from pydantic import BaseModel, BeforeValidator

T = TypeVar("T")


def logging_validator(value: T, /) -> T:
    print("Value:", value)

    return value


class Container(BaseModel, Generic[T]):
    item: T


IntContainer = Container[int]
LoggedContainer = Container[T]
# LoggedContainer = Annotated[Container[T], BeforeValidator(logging_validator)]


class Response(BaseModel):
    container: Container[int]
    # container: LoggedContainer[int]
    # containers: Sequence[LoggedContainer[int]]


response = Response(container=Container(item=123))

# value: LoggedContainer[int] = Container(item="not-an-int")

x: Container[int] = Container(item=123)
