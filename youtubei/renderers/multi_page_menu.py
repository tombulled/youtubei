from typing import Sequence

from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.multi_page_menu_section import MultiPageMenuSectionRenderer
from youtubei.renderers.privacy_tos_footer import PrivacyTosFooterRenderer

from ._base import BaseRenderer


@ANDROID_REGISTRY
@IOS_REGISTRY
class MultiPageMenuRenderer(BaseRenderer):
    sections: Sequence[Dynamic[MultiPageMenuSectionRenderer]]
    footer: Dynamic[PrivacyTosFooterRenderer]
