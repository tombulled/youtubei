from typing import Sequence, Union

from youtubei._registries import WEB_REGISTRY
from youtubei.enums import CountryCode
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.fusion_searchbox import FusionSearchboxRenderer
from youtubei.renderers.hotkey_dialog import HotkeyDialogRenderer
from youtubei.renderers.topbar_logo import TopbarLogoRenderer
from youtubei.renderers.topbar_menu_button import TopbarMenuButtonRenderer

from ._base import BaseRenderer

__all__ = ("DesktopTopbarRenderer",)


@WEB_REGISTRY
class DesktopTopbarRenderer(BaseRenderer):
    logo: Dynamic[TopbarLogoRenderer]
    searchbox: Dynamic[FusionSearchboxRenderer]
    country_code: CountryCode
    topbar_buttons: Sequence[Dynamic[Union[TopbarMenuButtonRenderer, ButtonRenderer]]]
    hotkey_dialog: Dynamic[HotkeyDialogRenderer]
    back_button: Dynamic[ButtonRenderer]
    forward_button: Dynamic[ButtonRenderer]
    a11y_skip_navigation_button: Dynamic[ButtonRenderer]
