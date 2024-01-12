from typing import Any, Mapping, Sequence, Union

from typing_extensions import TypeAlias

from .exceptions import ParseException

from . import utils
from .registry import RENDERERS

DataMap: TypeAlias = Mapping[str, Mapping[str, Any]]
DataSeq: TypeAlias = Sequence[DataMap]
Data: TypeAlias = Union[DataMap, DataSeq]


def parse_renderable(data: Data, /):
    assert utils.is_renderable(data)

    if isinstance(data, Sequence):
        return [parse_renderable(item) for item in data]

    key = next(iter(data))
    value = data[key]

    if key not in RENDERERS:
        raise ParseException(f"No renderer available for {key!r}")

    render_cls: type = RENDERERS[key]

    return render_cls.model_validate(value)
