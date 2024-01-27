from typing import Sequence, Union

from youtubei.models.base import BaseModel
from youtubei.renderers.background_promo import BackgroundPromoRenderer
from youtubei.renderers.compact_link import CompactLinkRenderer
from youtubei.renderers.privacy_tos_footer import PrivacyTosFooterRenderer
from youtubei.types import Dynamic, TrackingParams

from ._base import BaseRenderer


class MultiPageMenuSectionRenderer(BaseRenderer):
    items: Sequence[
        Dynamic[
            Union[
                BackgroundPromoRenderer,
                CompactLinkRenderer,
            ]
        ]
    ]


class MultiPageMenuRenderer(BaseRenderer):
    sections: Sequence[Dynamic[MultiPageMenuSectionRenderer]]
    footer: Dynamic[PrivacyTosFooterRenderer]
