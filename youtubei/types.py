from typing import Any, TypeVar

import pydantic
from typing_extensions import Annotated, TypeAlias

from youtubei.parse import parse

__all__ = (
    "BrowseId",
    "ClickTrackingParams",
    "TrackingParams",
)

T = TypeVar("T")

Renderable: TypeAlias = Annotated[Any, pydantic.BeforeValidator(parse)]
# KnownRenderable: TypeAlias = Annotated[T, pydantic.BeforeValidator(parse)]

BrowseId: TypeAlias = str
ClickTrackingParams: TypeAlias = str
TrackingParams: TypeAlias = str
