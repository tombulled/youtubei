from typing import Sequence

from youtubei.enums import TargetId
from youtubei.models.base import BaseModel
from youtubei.models.other import Icon
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.multi_page_menu import MultiPageMenuRenderer
from youtubei.types import Renderer, TrackingParams


class TopbarButtonRenderer(BaseModel):
    button_renderer: Renderer[ButtonRenderer]
    new_content_identifier: Sequence[str]


class TopbarLogoRenderer(BaseModel):
    icon_image: Icon
    tracking_params: str
    override_entity_key: str


class TopbarMenuButtonRenderer(BaseModel):
    icon: Icon
    menu_renderer: Renderer[MultiPageMenuRenderer]
    tracking_params: TrackingParams
    target_id: TargetId
