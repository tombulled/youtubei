from dataclasses import dataclass, field

from innertube import InnerTube

from .constants import CLIENT, PARSER
from .parser import WebRemixParser
from .responses import WebRemixGuideResponse


@dataclass
class WebRemix:
    parser: WebRemixParser = field(default=PARSER)
    client: InnerTube = field(default=CLIENT)

    def guide(self) -> WebRemixGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)
