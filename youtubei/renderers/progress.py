from youtubei.models.base import BaseModel
from youtubei.models.other import (
    CompletionBehaviorDuration,
    ErrorBehaviorUntilPageOrContainerSelected,
)


class UploadProgressArrowRenderer(BaseModel):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected
