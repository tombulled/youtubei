from typing import Optional, Sequence

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY, WEB_REGISTRY
from youtubei.enums import MultiPageMenuStyleType
from youtubei.parse import Dynamic
from youtubei.renderers.multi_page_menu_section import MultiPageMenuSectionRenderer
from youtubei.renderers.privacy_tos_footer import PrivacyTosFooterRenderer

from ._base import BaseRenderer

__all__ = ("MultiPageMenuRenderer",)


@WEB_REGISTRY
@ANDROID_REGISTRY
@IOS_REGISTRY
class MultiPageMenuRenderer(BaseRenderer):
    sections: Optional[Sequence[Dynamic[MultiPageMenuSectionRenderer]]] = None
    footer: Optional[Dynamic[PrivacyTosFooterRenderer]] = None
    style: Optional[MultiPageMenuStyleType] = None
    show_loading_spinner: Optional[bool] = None
