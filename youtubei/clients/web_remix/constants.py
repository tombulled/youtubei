from typing import Final

from innertube import InnerTube

from youtubei.clients.web_remix.registry import WEB_REMIX_REGISTRY

from .parser import WebRemixParser

WEB_REMIX_CLIENT_NAME: Final[str] = "WEB_REMIX"
WEB_REMIX_CLIENT_VERSION: Final[str] = "1.20231214.00.00"
WEB_REMIX_CLIENT: Final[InnerTube] = InnerTube(
    WEB_REMIX_CLIENT_NAME, WEB_REMIX_CLIENT_VERSION
)
WEB_REMIX_PARSER = WebRemixParser(WEB_REMIX_REGISTRY)
