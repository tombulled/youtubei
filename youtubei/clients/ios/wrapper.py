from dataclasses import dataclass, field

from innertube import InnerTube

from .constants import IOS_CLIENT, IOS_PARSER
from .parser import IosParser
from .responses import IosGuideResponse

__all__ = ("Ios",)


@dataclass
class Ios:
    parser: IosParser = field(default=IOS_PARSER)
    client: InnerTube = field(default=IOS_CLIENT)

    def __repr__(self) -> str:
        client_version: str = self.client.adaptor.context.client_version  # type: ignore

        return f"{type(self).__name__}({client_version!r})"

    def guide(self) -> IosGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)
