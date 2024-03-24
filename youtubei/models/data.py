from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseModel

__all__ = ("NextContinuationData",)


@WEB_REMIX_REGISTRY
class NextContinuationData(BaseModel):
    continuation: str
    click_tracking_params: str
