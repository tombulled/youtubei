from typing import Any, Sequence

from youtubei.models.text import Text
from youtubei.parse import Dynamic

from ._base import BaseRenderer

__all__ = ("CardCollectionRenderer",)


class CardCollectionRenderer(BaseRenderer):
    cards: Sequence[Dynamic]  # Observed: CardRenderer
    header_text: Text
    icon: Dynamic[Any]  # Observed: InfoCardIconRenderer
    close_button: Dynamic[Any]  # Observed: InfoCardIconRenderer
    allow_teaser_dismiss: bool
    log_icon_visibility_updates: bool
