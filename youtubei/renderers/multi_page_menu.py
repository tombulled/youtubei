from typing import Sequence, Union

from youtubei.models.base import BaseModel
from youtubei.renderers.background_promo import BackgroundPromoRenderer
from youtubei.renderers.compact_link import CompactLinkRenderer
from youtubei.renderers.privacy_tos_footer import PrivacyTosFooterRenderer
from youtubei.types import Renderer, TrackingParams


class MultiPageMenuSectionRenderer(BaseModel):
    tracking_params: TrackingParams
    items: Sequence[
        # Union[
        #     Renderer[BackgroundPromoRenderer],
        #     Renderer[CompactLinkRenderer],
        # ]
       Renderer[
            Union[
                BackgroundPromoRenderer,
                CompactLinkRenderer,
            ]
        ] 
    ]


class MultiPageMenuRenderer(BaseModel):
    sections: Sequence[Renderer[MultiPageMenuSectionRenderer]]
    tracking_params: TrackingParams
    footer: Renderer[PrivacyTosFooterRenderer]
