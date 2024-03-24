from typing import Sequence

from youtubei._registries import WEB_REGISTRY
from youtubei.enums import Privacy
from youtubei.models.endpoints import PlaylistEditEndpoint
from youtubei.models.other import EditableDetails, ShareData
from youtubei.models.text import ComplexText, SimpleText, Text
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.cinematic_container import CinematicContainerRenderer
from youtubei.renderers.hero_playlist_thumbnail import HeroPlaylistThumbnailRenderer
from youtubei.renderers.menu import MenuRenderer
from youtubei.renderers.playlist_byline import PlaylistBylineRenderer
from youtubei.renderers.toggle_button import ToggleButtonRenderer
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("PlaylistHeaderRenderer",)


@WEB_REGISTRY
class PlaylistHeaderRenderer(BaseRenderer):
    playlist_id: str
    title: SimpleText
    num_videos_text: ComplexText
    view_count_text: SimpleText
    share_data: ShareData
    is_editable: bool
    privacy: Privacy
    editable_details: EditableDetails
    service_endpoints: Sequence[DynamicCommand[PlaylistEditEndpoint]]
    stats: Sequence[Text]
    brief_stats: Sequence[ComplexText]
    playlist_header_banner: Dynamic[HeroPlaylistThumbnailRenderer]
    save_button: Dynamic[ToggleButtonRenderer]
    share_button: Dynamic[ButtonRenderer]
    more_actions_menu: Dynamic[MenuRenderer]
    subtitle: SimpleText
    play_button: Dynamic[ButtonRenderer]
    shuffle_play_button: Dynamic[ButtonRenderer]
    cinematic_container: Dynamic[CinematicContainerRenderer]
    byline: Sequence[Dynamic[PlaylistBylineRenderer]]
