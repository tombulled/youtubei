from dataclasses import dataclass, field

from innertube import InnerTube

from .constants import WEB_REMIX_CLIENT, WEB_REMIX_PARSER
from .parser import WebRemixParser
from .responses import WebRemixGuideResponse

__all__ = ("WebRemix",)


@dataclass
class WebRemix:
    parser: WebRemixParser = field(default=WEB_REMIX_PARSER)
    client: InnerTube = field(default=WEB_REMIX_CLIENT)

    def guide(self) -> WebRemixGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)
