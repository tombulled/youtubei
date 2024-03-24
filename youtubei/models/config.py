from youtubei._registries import IOS_MUSIC_REGISTRY, WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.enums import MusicPageType
from youtubei.enums.music import MusicVideoType
from youtubei.models.thumbnail import Thumbnails

from ._base import BaseModel

__all__ = (
    "BackgroundImageConfig",
    "BrowseEndpointContextMusicConfig",
    "CinematicContainerConfig",
    "ColourConfig",
    "CommonConfig",
    "Html5PlaybackOnesieConfig",
    "WebSearchboxConfig",
    "WatchEndpointMusicConfig",
)


class BackgroundImageConfig(BaseModel):
    thumbnail: Thumbnails


@WEB_REMIX_REGISTRY
@IOS_MUSIC_REGISTRY
class BrowseEndpointContextMusicConfig(BaseModel):
    page_type: MusicPageType


class CinematicContainerConfig(BaseModel):
    light_theme_background_color: int
    dark_theme_background_color: int
    color_source_size_multiplier: int
    apply_client_image_blur: bool


class ColourConfig(BaseModel):
    light_theme_color: int
    dark_theme_color: int
    start_location: float


class CommonConfig(BaseModel):
    url: str


@WEB_REGISTRY
class Html5PlaybackOnesieConfig(BaseModel):
    commonConfig: CommonConfig


@WEB_REGISTRY
class WebSearchboxConfig(BaseModel):
    request_language: str
    request_domain: str
    has_onscreen_keyboard: bool
    focus_searchbox: bool


@WEB_REMIX_REGISTRY
class WatchEndpointMusicConfig(BaseModel):
    music_video_type: MusicVideoType
