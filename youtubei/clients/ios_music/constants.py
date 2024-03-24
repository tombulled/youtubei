from typing import Final

from innertube import InnerTube

from youtubei._registries import IOS_MUSIC_REGISTRY

from .parser import IosMusicParser

__all__ = (
    "IOS_MUSIC_CLIENT_NAME",
    "IOS_MUSIC_CLIENT_VERSION",
    "IOS_MUSIC_CLIENT",
    "IOS_MUSIC_PARSER",
)

IOS_MUSIC_CLIENT_NAME: Final[str] = "IOS_MUSIC"
IOS_MUSIC_CLIENT_VERSION: Final[str] = "6.33.3"
IOS_MUSIC_CLIENT: Final[InnerTube] = InnerTube(
    IOS_MUSIC_CLIENT_NAME, IOS_MUSIC_CLIENT_VERSION
)
IOS_MUSIC_PARSER: Final[IosMusicParser] = IosMusicParser(IOS_MUSIC_REGISTRY)
