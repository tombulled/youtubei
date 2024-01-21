from typing import Optional, Sequence
from ._base import BaseModel


class ServiceTrackingParam(BaseModel):
    key: str
    value: str


class ServiceTrackingParams(BaseModel):
    service: str
    params: Sequence[ServiceTrackingParam]


class MainAppWebResponseContext(BaseModel):
    logged_out: bool
    tracking_param: str


class WebResponseContextExtensionData(BaseModel):
    has_decorated: bool


class ResponseContext(BaseModel):
    visitor_data: str
    service_tracking_params: Sequence[ServiceTrackingParams]
    max_age_seconds: Optional[int] = None
    main_app_web_response_context: Optional[MainAppWebResponseContext] = None
    web_response_context_extension_data: Optional[
        WebResponseContextExtensionData
    ] = None