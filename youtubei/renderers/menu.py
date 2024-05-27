from typing import Optional, Sequence, Union

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.accessibility import Accessibility
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.like_button import LikeButtonRenderer
from youtubei.renderers.menu_navigation_item import MenuNavigationItemRenderer
from youtubei.renderers.menu_service_item import MenuServiceItemRenderer
from youtubei.renderers.toggle_button import ToggleButtonRenderer
from youtubei.renderers.toggle_menu_service_item import ToggleMenuServiceItemRenderer

from ._base import BaseRenderer

__all__ = ("MenuRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class MenuRenderer(BaseRenderer):
    items: Optional[
        Sequence[
            Dynamic[
                Union[
                    MenuNavigationItemRenderer,
                    MenuServiceItemRenderer,
                    ToggleMenuServiceItemRenderer,
                ]
            ]
        ]
    ] = None
    open_immediately: Optional[bool] = None
    top_level_buttons: Optional[
        Sequence[
            Dynamic[
                Union[
                    ToggleButtonRenderer,
                    ButtonRenderer,
                    LikeButtonRenderer,
                ]
            ]
        ]
    ] = None
    accessibility: Optional[Accessibility] = None
