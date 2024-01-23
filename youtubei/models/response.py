from typing import Sequence
from youtubei.models.base import BaseModel


class Param(BaseModel):
    key: str
    value: str


class ServiceTrackingParams(BaseModel):
    service: str
    params: Sequence[Param]


class ResponseContext(BaseModel):
    visitor_data: str
    service_tracking_params: Sequence[ServiceTrackingParams]


class Response(BaseModel):
    tracking_params: str
    response_context: ResponseContext