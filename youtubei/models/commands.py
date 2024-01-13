from youtubei.models.endpoints import UrlEndpoint, WebviewEndpoint
from youtubei.types import ClickTrackingParams

from ._base import BaseModel

__all__ = (
    "PrivacyCommand",
    "TosCommand",
)


class PrivacyCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    url_endpoint: UrlEndpoint


class TosCommand(BaseModel):
    click_tracking_params: ClickTrackingParams
    webview_endpoint: WebviewEndpoint
