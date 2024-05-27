from typing import Sequence
from youtubei.models.endpoints import BrowseEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.music_card_shelf_header_basic import (
    MusicCardShelfHeaderBasicRenderer,
)
from youtubei.renderers.music_responsive_list_item import (
    MusicResponsiveListItemRenderer,
)
from youtubei.renderers.music_thumbnail import MusicThumbnailRenderer
from youtubei.validated_types import DynamicCommand
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("MusicCardShelfRenderer",)


@WEB_REMIX_REGISTRY
class MusicCardShelfRenderer(BaseRenderer):
    thumbnail: Dynamic[MusicThumbnailRenderer]
    title: ComplexText
    subtitle: ComplexText
    contents: Sequence[Dynamic[MusicResponsiveListItemRenderer]]
    buttons: Sequence[Dynamic[ButtonRenderer]]
    menu: Dynamic[MenuRenderer]
    on_tap: DynamicCommand[BrowseEndpoint]
    header: Dynamic[MusicCardShelfHeaderBasicRenderer]
    end_icon: Icon
