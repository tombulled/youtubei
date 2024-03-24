from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.topbar_button import TopbarButtonRenderer
from youtubei.renderers.topbar_logo import TopbarLogoRenderer
from youtubei.renderers.topbar_menu_button import TopbarMenuButtonRenderer

from ._base import BaseRenderer

__all__ = ("MobileTopbarRenderer",)


TopbarButton: TypeAlias = Dynamic[
    Union[
        ButtonRenderer,
        TopbarButtonRenderer,
        TopbarMenuButtonRenderer,
    ]
]


@ANDROID_REGISTRY
@IOS_REGISTRY
class MobileTopbarRenderer(BaseRenderer):
    placeholder_text: Text
    buttons: Sequence[TopbarButton]
    controls_cast_button: bool
    topbar_logo: Dynamic[TopbarLogoRenderer]
