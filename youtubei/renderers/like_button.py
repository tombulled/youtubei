from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.models.endpoints import ModalEndpoint
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class LikeButtonRenderer(BaseRenderer):
    dislike_navigation_endpoint: DynamicCommand[ModalEndpoint]
    like_command: DynamicCommand[ModalEndpoint]
