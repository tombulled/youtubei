from youtubei._registries import IOS_REGISTRY
from youtubei.models.other import (
    CompletionBehaviorDuration,
    ErrorBehaviorUntilPageOrContainerSelected,
)

from ._base import BaseRenderer

__all__ = ("UploadProgressArrowRenderer",)


@IOS_REGISTRY
class UploadProgressArrowRenderer(BaseRenderer):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: (
        ErrorBehaviorUntilPageOrContainerSelected
    )
