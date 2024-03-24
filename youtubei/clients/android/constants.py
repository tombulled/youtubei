from typing import Final

from innertube import InnerTube

from youtubei._registries import ANDROID_REGISTRY

from .parser import AndroidParser

__all__ = (
    "ANDROID_CLIENT_NAME",
    "ANDROID_CLIENT_VERSION",
    "ANDROID_CLIENT",
    "ANDROID_PARSER",
)

ANDROID_CLIENT_NAME: Final[str] = "ANDROID"
ANDROID_CLIENT_VERSION: Final[str] = "19.03.35"
ANDROID_CLIENT: Final[InnerTube] = InnerTube(
    ANDROID_CLIENT_NAME, ANDROID_CLIENT_VERSION
)
ANDROID_PARSER: Final[AndroidParser] = AndroidParser(ANDROID_REGISTRY)
