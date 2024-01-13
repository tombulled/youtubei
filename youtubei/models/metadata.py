from typing import Optional

from youtubei.enums import WebPageType

from ._base import BaseModel

__all__ = (
    "WebCommandMetadata",
    "CommandMetadata",
)


class WebCommandMetadata(BaseModel):
    url: Optional[str] = None
    web_page_type: Optional[WebPageType] = None
    root_ve: Optional[int] = None
    api_url: Optional[str] = None
    send_post: Optional[bool] = None


class CommandMetadata(BaseModel):
    web_command_metadata: WebCommandMetadata
