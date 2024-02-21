from typing import Sequence

from youtubei.models.text import Text
from youtubei.parse import Dynamic

from ._base import BaseRenderer


class CardCollectionRenderer(BaseRenderer):
    cards: Sequence[Dynamic]  # CardRenderer
    header_text: Text
    icon: Dynamic  # InfoCardIconRenderer
    close_button: Dynamic  # InfoCardIconRenderer
    allow_teaser_dismiss: bool
    log_icon_visibility_updates: bool
