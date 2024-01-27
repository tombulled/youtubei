from typing import Sequence

from youtubei.enums import TargetId
from youtubei.models.other import Icon
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.multi_page_menu import MultiPageMenuRenderer
from youtubei.types import Dynamic, TrackingParams
from ._base import BaseRenderer


class TopbarButtonRenderer(BaseRenderer):
    button_renderer: Dynamic[ButtonRenderer]
    new_content_identifier: Sequence[str]


class TopbarLogoRenderer(BaseRenderer):
    icon_image: Icon
    override_entity_key: str


class TopbarMenuButtonRenderer(BaseRenderer):
    icon: Icon
    menu_renderer: Dynamic[MultiPageMenuRenderer]
    target_id: TargetId
