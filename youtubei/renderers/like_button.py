from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.models.endpoints import ModalEndpoint
from youtubei.models.other import LikeButtonTarget
from youtubei.validated_types import DynamicCommand
from youtubei.enums import LikeStatus

from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class LikeButtonRenderer(BaseRenderer):
    target: LikeButtonTarget
    like_status: LikeStatus
    likes_allowed: bool
    dislike_navigation_endpoint: DynamicCommand[ModalEndpoint]
    like_command: DynamicCommand[ModalEndpoint]
