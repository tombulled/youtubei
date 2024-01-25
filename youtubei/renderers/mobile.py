from typing import Sequence, Union

from youtubei.models.base import BaseModel
from youtubei.models.text import Text
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.topbar import (
    TopbarButtonRenderer,
    TopbarLogoRenderer,
    TopbarMenuButtonRenderer,
)
from youtubei.types import Renderer, TrackingParams


class MobileTopbarRenderer(BaseModel):
    placeholder_text: Text
    tracking_params: TrackingParams
    buttons: Sequence[
        # Union[
        #     Renderer[ButtonRenderer],
        #     Renderer[TopbarButtonRenderer],
        #     Renderer[TopbarMenuButtonRenderer],
        # ]
        Renderer[
            Union[
                ButtonRenderer,
                TopbarButtonRenderer,
                TopbarMenuButtonRenderer,
            ]
        ]
    ]
    controls_cast_button: bool
    topbar_logo: Renderer[TopbarLogoRenderer]
