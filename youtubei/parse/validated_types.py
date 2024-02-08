from typing import (
    Any,
    Generic,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    TypeVar,
    Annotated,
    TypeAlias,
)

from pydantic import BaseModel, BeforeValidator, TypeAdapter, ValidationInfo

from pydantic.dataclasses import dataclass
# from dataclasses import dataclass

# from typing_extensions import Annotated, TypeAlias

from .validators import ContainerValidator, validate_dynamic

__all__ = ("Dynamic",)

T = TypeVar("T")


# class Command(BaseModel, Generic[T]):
@dataclass
class Command(Generic[T]):
    tracking_params: str
    command: T
    # target: Any
    # action: Optional[Any] = None
    # endpoint: Optional[Any] = None


def validate_command(
    obj: Any,
    validation_info: ValidationInfo,
) -> Any:
    suffixes: Set[str] = {"endpoint", "action"}

    if not isinstance(obj, Mapping):
        return obj

    rich_matches: Sequence[Tuple[str, str]] = [
        (key, suffix.lower())
        for key in obj
        for suffix in suffixes
        if key.lower().endswith(suffix.lower())
    ]

    assert len(rich_matches) == 1

    rich_key, suffix = rich_matches[0]
    rich_value = obj[rich_key]
    rich_obj = validate_dynamic({rich_key: rich_value}, validation_info)

    new_obj = {key: value for key, value in obj.items() if key != rich_key}

    new_obj["command"] = rich_obj
    # new_obj[suffix] = rich_obj

    # return Command.model_validate(
    #     new_obj,
    #     context=validation_info.context,
    # )

    # return TypeAdapter(Command).validate_python(
    #     new_obj,
    #     context=validation_info.context,
    # )

    # return Command(tracking_params="tp", command=rich_obj)

    return new_obj


# DynamicCommand: TypeAlias = Command[T]
# DynamicCommand: TypeAlias = Annotated[Command[T], "hey"]
DynamicCommand: TypeAlias = Annotated[
    # Any,
    Command[T],
    BeforeValidator(
        validate_command,
        # ContainerValidator(
        #     container_cls=Command,
        #     field="command",
        #     suffixes={"endpoint", "action"},
        # ),
    ),
]
Dynamic: TypeAlias = Annotated[T, BeforeValidator(validate_dynamic)]
