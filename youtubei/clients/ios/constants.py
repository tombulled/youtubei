from typing import Final

from innertube import InnerTube

from youtubei._registries import IOS_REGISTRY

from .parser import IosParser

IOS_CLIENT_NAME: Final[str] = "IOS"
IOS_CLIENT_VERSION: Final[str] = "18.49.3"
IOS_CLIENT: Final[InnerTube] = InnerTube(IOS_CLIENT_NAME, IOS_CLIENT_VERSION)
IOS_PARSER = IosParser(IOS_REGISTRY)
