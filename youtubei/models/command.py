from typing import Generic, Optional, TypeVar, Union

from pydantic.dataclasses import dataclass

from youtubei.models.metadata import (
    InteractionLoggingCommandMetadata,
    WebCommandMetadata,
)
from youtubei.parse.validated_types import Dynamic

from .base import BaseModel

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
        * hack=True
    Notes:
        * Only endpoints have been observed to have command metadata
    """

    # Potential properties: is_endpoint, is_action, is_command, is_hack

    click_tracking_params: str
    command_metadata: Optional[
        Dynamic[
            Union[
                WebCommandMetadata,
                InteractionLoggingCommandMetadata,
            ]
        ]
    ] = None
    # hack: Optional[bool] = None
    command: Optional[T] = (
        None  # Todo: Change to Union[BaseEndpoint, BaseAction, BaseCommand]?
    )
