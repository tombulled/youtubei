from typing import Optional

from youtubei._registries import WEB_REGISTRY
from youtubei.enums import WebPageType
from youtubei.models.logging import LoggingExpectations

from ._base import BaseModel

__all__ = (
    "InteractionLoggingCommandMetadata",
    "WebCommandMetadata",
)


class InteractionLoggingCommandMetadata(BaseModel):
    logging_expectations: LoggingExpectations


@WEB_REGISTRY
class WebCommandMetadata(BaseModel):
    url: Optional[str] = None
    web_page_type: Optional[WebPageType] = None
    root_ve: Optional[int] = None
    api_url: Optional[str] = None
    send_post: Optional[bool] = None
    ignore_navigation: Optional[bool] = None
