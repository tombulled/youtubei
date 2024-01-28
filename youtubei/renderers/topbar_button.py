from typing import Sequence

from youtubei._registries import IOS_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer

from ._base import BaseRenderer

from youtubei._registries import ANDROID_REGISTRY

@ANDROID_REGISTRY
@IOS_REGISTRY
class TopbarButtonRenderer(BaseRenderer):
    button_renderer: Dynamic[ButtonRenderer]
    new_content_identifier: Sequence[str]
