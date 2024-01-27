from typing import Sequence, Union

from youtubei.models.base import BaseModel
from youtubei.models.text import Text
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.topbar import (
    TopbarButtonRenderer,
    TopbarLogoRenderer,
    TopbarMenuButtonRenderer,
)
from youtubei.types import Dynamic, TrackingParams
from ._base import BaseRenderer


class MobileTopbarRenderer(BaseRenderer):
    placeholder_text: Text
    buttons: Sequence[
        Dynamic[
            Union[
                ButtonRenderer,
                TopbarButtonRenderer,
                TopbarMenuButtonRenderer,
            ]
        ]
    ]
    controls_cast_button: bool
    topbar_logo: Dynamic[TopbarLogoRenderer]
