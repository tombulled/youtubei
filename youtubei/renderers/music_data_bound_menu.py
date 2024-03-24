from typing import Sequence

from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.models.data_bound import DataBoundMenuItem, DataBoundTopLevelMenuButton
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.menu import MenuRenderer

from ._base import BaseRenderer

__all__ = ("MusicDataBoundMenuRenderer",)


@WEB_REMIX_REGISTRY
class MusicDataBoundMenuRenderer(BaseRenderer):
    menu_renderer_mold: Dynamic[MenuRenderer]
    data_bound_menu_items: Sequence[DataBoundMenuItem]
    data_bound_top_level_menu_buttons: Sequence[DataBoundTopLevelMenuButton]
