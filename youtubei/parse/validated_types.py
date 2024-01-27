from typing import TypeVar

from pydantic import BeforeValidator
from typing_extensions import Annotated, TypeAlias

from .validators import validate_dynamic

__all__ = ("Dynamic",)

T = TypeVar("T")

Dynamic: TypeAlias = Annotated[T, BeforeValidator(validate_dynamic)]
