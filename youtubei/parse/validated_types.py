from typing import Any, Generic, Optional, TypeVar

from pydantic import BaseModel, BeforeValidator
from typing_extensions import Annotated, TypeAlias

from .validators import ContainerValidator, validate_dynamic

__all__ = ("Dynamic",)

T = TypeVar("T")


class Command(BaseModel, Generic[T]):
    tracking_params: str
    command: T
    # target: Any
    # action: Optional[Any] = None
    # endpoint: Optional[Any] = None


DynamicCommand: TypeAlias = Annotated[
    Any,
    # Command[T],
    BeforeValidator(
        ContainerValidator(
            container_cls=Command,
            field="command",
            suffixes={"endpoint", "action"},
        ),
    ),
]
Dynamic: TypeAlias = Annotated[T, BeforeValidator(validate_dynamic)]
