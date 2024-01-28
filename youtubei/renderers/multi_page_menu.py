from typing import Sequence, Union

from youtubei._registries import IOS_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.background_promo import BackgroundPromoRenderer
from youtubei.renderers.compact_link import CompactLinkRenderer
from youtubei.renderers.privacy_tos_footer import PrivacyTosFooterRenderer

from ._base import BaseRenderer


@IOS_REGISTRY
class MultiPageMenuSectionRenderer(BaseRenderer):
    items: Sequence[
        Dynamic[
            Union[
                BackgroundPromoRenderer,
                CompactLinkRenderer,
            ]
        ]
    ]


@IOS_REGISTRY
class MultiPageMenuRenderer(BaseRenderer):
    sections: Sequence[Dynamic[MultiPageMenuSectionRenderer]]
    footer: Dynamic[PrivacyTosFooterRenderer]
