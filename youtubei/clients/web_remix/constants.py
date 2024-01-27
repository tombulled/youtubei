from typing import Final

from innertube import InnerTube
from youtubei.clients.web_remix.registry import WEB_REMIX_REGISTRY

from youtubei.parse.types import MutableRegistryMapping

from .parser import WebRemixParser

CLIENT_NAME: Final[str] = "WEB_REMIX"
CLIENT_VERSION: Final[str] = "1.20231214.00.00"

CLIENT: Final[InnerTube] = InnerTube(CLIENT_NAME, CLIENT_VERSION)
PARSER = WebRemixParser(WEB_REMIX_REGISTRY)
