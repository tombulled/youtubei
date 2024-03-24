from typing import Final

from innertube import InnerTube

from youtubei._registries import IOS_REGISTRY

from .parser import IosParser

__all__ = (
    "IOS_CLIENT_NAME",
    "IOS_CLIENT_VERSION",
    "IOS_CLIENT",
    "IOS_PARSER",
)

IOS_CLIENT_NAME: Final[str] = "IOS"
IOS_CLIENT_VERSION: Final[str] = "18.49.3"
IOS_CLIENT: Final[InnerTube] = InnerTube(IOS_CLIENT_NAME, IOS_CLIENT_VERSION)
IOS_PARSER: Final[IosParser] = IosParser(IOS_REGISTRY)
