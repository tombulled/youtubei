from typing import Sequence
from youtubei.models import BaseModel


class Param(BaseModel):
    key: str
    value: str


class ServiceTrackingParams(BaseModel):
    service: str
    params: Sequence[Param]


class MainAppWebResponseContext(BaseModel):
    logged_out: bool
    tracking_param: str


class WebResponseContextExtensionData(BaseModel):
    has_decorated: bool


class WebResponseContext(BaseModel):
    visitor_data: str
    service_tracking_params: Sequence[ServiceTrackingParams]
    max_age_seconds: int
    main_app_web_response_context: MainAppWebResponseContext
    web_response_context_extension_data: WebResponseContextExtensionData
