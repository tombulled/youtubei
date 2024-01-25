from typing import Optional

from youtubei.enums import WebPageType
from youtubei.models.logging import LoggingExpectations

from .base import BaseModel

__all__ = (
    "WebCommandMetadata",
    "CommandMetadata",
)


class InteractionLoggingCommandMetadata(BaseModel):
    logging_expectations: LoggingExpectations


class WebCommandMetadata(BaseModel):
    url: Optional[str] = None
    web_page_type: Optional[WebPageType] = None
    root_ve: Optional[int] = None
    api_url: Optional[str] = None
    send_post: Optional[bool] = None


class CommandMetadata(BaseModel):
    web_command_metadata: WebCommandMetadata
    interaction_logging_command_metadata: Optional[
        InteractionLoggingCommandMetadata
    ] = None
