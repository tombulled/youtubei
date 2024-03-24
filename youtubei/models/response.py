from typing import Mapping, Optional, Sequence, Tuple

from youtubei.models._base import BaseModel

__all__ = (
    "Parameter",
    "ServiceTrackingParams",
    "ResponseContext",
    "Response",
)


class Parameter(BaseModel):
    key: str
    value: str

    def as_tuple(self) -> Tuple[str, str]:
        return (self.key, self.value)


class ServiceTrackingParams(BaseModel):
    service: str
    params: Sequence[Parameter]

    def as_dict(self) -> Mapping[str, str]:
        return {parameter.key: parameter.value for parameter in self.params}


class ResponseContext(BaseModel):
    visitor_data: Optional[str] = None
    service_tracking_params: Sequence[ServiceTrackingParams]

    @property
    def parameters(self) -> Mapping[str, Mapping[str, str]]:
        return {
            service_tracking_params.service: service_tracking_params.as_dict()
            for service_tracking_params in self.service_tracking_params
        }


class Response(BaseModel):
    tracking_params: Optional[str] = None
    response_context: ResponseContext
