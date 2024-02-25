from .base import BaseModel
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class NextContinuationData(BaseModel):
    continuation: str
    click_tracking_params: str
