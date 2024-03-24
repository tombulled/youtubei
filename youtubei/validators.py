from typing import Any, Mapping, Sequence, Set

from pydantic import ValidationInfo

from youtubei.models._base import BaseModel
from youtubei.parse.validators import validate_dynamic

__all__ = ("validate_command",)


# TODO: Find a better home for this class?
class _HackEndpoint(BaseModel):
    pass


def validate_command(
    obj: Any,
    validation_info: ValidationInfo,
) -> Any:
    suffixes: Set[str] = {"endpoint", "action", "command"}
    field: str = "command"

    if not isinstance(obj, Mapping):
        return obj

    rich_matches: Sequence[str] = [
        key
        for key in obj
        for suffix in suffixes
        if key.lower().endswith(suffix.lower())
    ]

    assert len(rich_matches) == 1

    rich_key = rich_matches[0]
    rich_value = obj[rich_key]

    if rich_value.get("hack", False):
        rich_obj = _HackEndpoint()
    else:
        rich_obj = validate_dynamic({rich_key: rich_value}, validation_info)

    new_obj = {key: value for key, value in obj.items() if key != rich_key}

    new_obj[field] = rich_obj

    return new_obj
