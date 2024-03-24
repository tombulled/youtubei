from typing import Generic, Optional, TypeVar, Union

from pydantic.dataclasses import dataclass

from youtubei.models.metadata import (
    InteractionLoggingCommandMetadata,
    WebCommandMetadata,
)
from youtubei.parse.validated_types import Dynamic

from ._base import BaseModel

__all__ = ("Command",)

T = TypeVar("T")


# Note: This is a custom container type
# Note: This is deliberately not extending BaseModel
#   as generic models don't play well with Annotated[]
@dataclass(config=BaseModel.model_config)
class Command(Generic[T]):
    """
    Command's contain either:
        * 1x endpoint
        * 1x action
        * hack=True (handled by validate_command, which yields _HackEndpoint)
    Notes:
        * Only endpoints have been observed to have command metadata
    """

    click_tracking_params: str
    command_metadata: Optional[
        Dynamic[
            Union[
                WebCommandMetadata,
                InteractionLoggingCommandMetadata,
            ]
        ]
    ] = None
    command: Optional[T] = None
