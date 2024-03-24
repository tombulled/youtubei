from typing import Final

from innertube import InnerTube

from youtubei._registries import WEB_REGISTRY

from .parser import WebParser

__all__ = (
    "WEB_CLIENT_NAME",
    "WEB_CLIENT_VERSION",
    "WEB_CLIENT",
    "WEB_PARSER",
)

WEB_CLIENT_NAME: Final[str] = "WEB"
WEB_CLIENT_VERSION: Final[str] = "2.20240105.01.00"
WEB_CLIENT: Final[InnerTube] = InnerTube(WEB_CLIENT_NAME, WEB_CLIENT_VERSION)
WEB_PARSER: Final[WebParser] = WebParser(WEB_REGISTRY)
