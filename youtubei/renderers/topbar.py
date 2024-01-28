from typing import Sequence

from youtubei._registries import IOS_REGISTRY
from youtubei.enums import TargetId
from youtubei.models.other import Icon
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.multi_page_menu import MultiPageMenuRenderer

from ._base import BaseRenderer


@IOS_REGISTRY
class TopbarButtonRenderer(BaseRenderer):
    button_renderer: Dynamic[ButtonRenderer]
    new_content_identifier: Sequence[str]


@IOS_REGISTRY
class TopbarLogoRenderer(BaseRenderer):
    icon_image: Icon
    override_entity_key: str


@IOS_REGISTRY
class TopbarMenuButtonRenderer(BaseRenderer):
    icon: Icon
    menu_renderer: Dynamic[MultiPageMenuRenderer]
    target_id: TargetId
