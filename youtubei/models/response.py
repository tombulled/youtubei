from typing import Sequence

from youtubei.models.base import BaseModel


class Parameter(BaseModel):
    key: str
    value: str


class ServiceTrackingParams(BaseModel):
    service: str
    params: Sequence[Parameter]


class ResponseContext(BaseModel):
    visitor_data: str
    service_tracking_params: Sequence[ServiceTrackingParams]


class Response(BaseModel):
    tracking_params: str
    response_context: ResponseContext
