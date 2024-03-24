from dataclasses import dataclass, field

from innertube import InnerTube

from .constants import ANDROID_CLIENT, ANDROID_PARSER
from .parser import AndroidParser
from .responses import AndroidGuideResponse

__all__ = ("Android",)


@dataclass
class Android:
    parser: AndroidParser = field(default=ANDROID_PARSER)
    client: InnerTube = field(default=ANDROID_CLIENT)

    def __repr__(self) -> str:
        client_version: str = self.client.adaptor.context.client_version  # type: ignore

        return f"{type(self).__name__}({client_version!r})"

    def guide(self) -> AndroidGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)
