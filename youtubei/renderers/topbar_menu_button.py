from youtubei._registries import IOS_REGISTRY
from youtubei.enums import TargetId
from youtubei.models.other import Icon
from youtubei.parse import Dynamic
from youtubei.renderers.multi_page_menu import MultiPageMenuRenderer

from ._base import BaseRenderer

from youtubei._registries import ANDROID_REGISTRY

@ANDROID_REGISTRY
@IOS_REGISTRY
class TopbarMenuButtonRenderer(BaseRenderer):
    icon: Icon
    menu_renderer: Dynamic[MultiPageMenuRenderer]
    target_id: TargetId
