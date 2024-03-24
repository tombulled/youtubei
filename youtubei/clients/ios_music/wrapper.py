from dataclasses import dataclass, field

from innertube import InnerTube

from .constants import IOS_MUSIC_CLIENT, IOS_MUSIC_PARSER
from .parser import IosMusicParser
from .responses import IosMusicGuideResponse

__all__ = ("IosMusic",)


@dataclass
class IosMusic:
    parser: IosMusicParser = field(default=IOS_MUSIC_PARSER)
    client: InnerTube = field(default=IOS_MUSIC_CLIENT)

    def __repr__(self) -> str:
        client_version: str = self.client.adaptor.context.client_version  # type: ignore

        return f"{type(self).__name__}({client_version!r})"

    def guide(self) -> IosMusicGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)
