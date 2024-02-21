from typing import Annotated, TypeAlias, TypeVar

from pydantic import BeforeValidator

from .validators import validate_dynamic

__all__ = ("Dynamic",)

T = TypeVar("T")

Dynamic: TypeAlias = Annotated[T, BeforeValidator(validate_dynamic)]
