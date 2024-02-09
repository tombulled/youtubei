from typing import Annotated, TypeAlias, TypeVar

from pydantic import BeforeValidator

from youtubei.models.command import Command
from youtubei.validators import validate_command

__all__ = ("DynamicCommand",)

T = TypeVar("T")

DynamicCommand: TypeAlias = Annotated[
    Command[T],
    BeforeValidator(
        validate_command,
    ),
]
