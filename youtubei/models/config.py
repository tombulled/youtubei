from youtubei._registries import IOS_MUSIC_REGISTRY
from youtubei.enums import MusicPageType

from .base import BaseModel


@IOS_MUSIC_REGISTRY
class BrowseEndpointContextMusicConfig(BaseModel):
    page_type: MusicPageType
