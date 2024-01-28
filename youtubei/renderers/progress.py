from youtubei.models.base import BaseModel
from youtubei.models.other import (
    CompletionBehaviorDuration,
    ErrorBehaviorUntilPageOrContainerSelected,
)
from youtubei._registries import IOS_REGISTRY

from ._base import BaseRenderer

@IOS_REGISTRY
class UploadProgressArrowRenderer(BaseRenderer):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected
