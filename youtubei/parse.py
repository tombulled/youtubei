import re
from typing import Any, Mapping, Sequence, Union

from rich.pretty import pprint
from typing_extensions import TypeAlias

from . import utils
from .exceptions import ParseException
from .registry import RENDERERS

__all__ = ("parse",)

# DataMap: TypeAlias = Mapping[str, Mapping[str, Any]]
# DataSeq: TypeAlias = Sequence[DataMap]
# Data: TypeAlias = Union[DataMap, DataSeq]

Primitive: TypeAlias = Union[
    str,
    int,
    float,
    bool,
    None,
]
Object: TypeAlias = Mapping[str, "ParseableData"]
Array: TypeAlias = Sequence["ParseableData"]
ParseableData: TypeAlias = Union[
    Primitive,
    Object,
    Array,
]


def _is_renderable(data: Any, /) -> bool:
    """
    >>> is_renderable({"FooRenderer": {}})
    True
    >>> is_renderable({})
    False
    """

    # if isinstance(data, Sequence):
    #     return all(map(is_renderable, data))

    if not isinstance(data, Mapping):
        return False

    if len(data) != 1:
        return False

    key: Any = next(iter(data))
    value: Any = data[key]

    if not isinstance(key, str):
        return False

    if not re.match(r"(.+)Renderer", key):
        return False

    if not isinstance(value, Mapping):
        return False

    return True


def parse(data, /):
    if utils.is_primitive(data):
        return data

    if isinstance(data, Sequence):
        return [parse(item) for item in data]

    assert isinstance(data, Mapping)

    if not _is_renderable(data):
        return {key: parse(value) for key, value in data.items()}

    key = next(iter(data))
    value = data[key]

    # FIXME: TEMP HOTFIX TO POPULATE RENDERERS
    from . import renderers

    if key not in RENDERERS:
        # TODO: Remove me, or make DEBUG
        pprint(value)

        raise ParseException(f"No renderer available for {key!r}")

    render_cls: type = RENDERERS[key]

    try:
        return render_cls.model_validate(value)
    except Exception as error:
        # TODO: Remove me, or make DEBUG
        pprint(value)

        raise error
