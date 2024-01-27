from typing import Any, TypeVar

import pydantic
from typing_extensions import Annotated, TypeAlias

from youtubei.parser import Parser
from youtubei.utils import first_entry

# from youtubei.parser import Parser
# from youtubei.webremix.registry import WEB_REMIX_REGISTRY

T = TypeVar("T")


def _parse(value: Any, info: pydantic.ValidationInfo):
    context = info.context

    assert context

    # todo: raise if not present
    registry = context["registry"]

    # parser = Parser(registry)

    # return parser.parse(value)

    key, val = first_entry(value)

    cls = registry.get(key)

    return pydantic.TypeAdapter(cls).validate_python(val, context=context)


Dynamic: TypeAlias = Annotated[
    # T, pydantic.BeforeValidator(Parser(WEB_REMIX_REGISTRY).parse)
    T,
    pydantic.BeforeValidator(_parse),
]

ClickTrackingParams: TypeAlias = str
TrackingParams: TypeAlias = str
BrowseId: TypeAlias = str
