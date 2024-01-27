from youtubei.models.base import BaseModel
from youtubei.models.other import (
    CompletionBehaviorDuration,
    ErrorBehaviorUntilPageOrContainerSelected,
)

from ._base import BaseRenderer


class UploadProgressArrowRenderer(BaseRenderer):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected
