from typing import Any

import pydantic
from typing_extensions import Annotated, TypeAlias

from youtubei.parse import parse

__all__ = (
    "BrowseId",
    "ClickTrackingParams",
    "TrackingParams",
)

Renderable = Annotated[Any, pydantic.BeforeValidator(parse)]

BrowseId: TypeAlias = str
ClickTrackingParams: TypeAlias = str
TrackingParams: TypeAlias = str
