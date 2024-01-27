from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.topbar import (
    TopbarButtonRenderer,
    TopbarLogoRenderer,
    TopbarMenuButtonRenderer,
)

from ._base import BaseRenderer

TopbarButton: TypeAlias = Dynamic[
    Union[
        ButtonRenderer,
        TopbarButtonRenderer,
        TopbarMenuButtonRenderer,
    ]
]


class MobileTopbarRenderer(BaseRenderer):
    placeholder_text: Text
    buttons: Sequence[TopbarButton]
    controls_cast_button: bool
    topbar_logo: Dynamic[TopbarLogoRenderer]
