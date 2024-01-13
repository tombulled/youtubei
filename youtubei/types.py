from typing import Any
from typing_extensions import Annotated, TypeAlias

import pydantic

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
