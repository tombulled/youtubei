from dataclasses import dataclass, field

from innertube import InnerTube

from .constants import WEB_REMIX_CLIENT, WEB_REMIX_PARSER
from .parser import WebRemixParser
from .responses import WebRemixConfigResponse, WebRemixGuideResponse

__all__ = ("WebRemix",)


@dataclass
class WebRemix:
    parser: WebRemixParser = field(default=WEB_REMIX_PARSER)
    client: InnerTube = field(default=WEB_REMIX_CLIENT)

    def __repr__(self) -> str:
        client_version: str = self.client.adaptor.context.client_version

        return f"{type(self).__name__}({client_version!r})"

    def config(self) -> WebRemixConfigResponse:
        response: dict = self.client.adaptor.dispatch("config")

        return self.parser.config(response)

    def guide(self) -> WebRemixGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)
