from .._registries import WEB_REMIX_REGISTRY
from .base import BaseModel


@WEB_REMIX_REGISTRY
class NextContinuationData(BaseModel):
    continuation: str
    click_tracking_params: str
