from dataclasses import dataclass, field

from innertube import InnerTube

from .constants import WEB_CLIENT, WEB_PARSER
from .parser import WebParser
from .responses import WebBrowseResponse, WebGuideResponse

__all__ = ("Web",)


@dataclass
class Web:
    parser: WebParser = field(default=WEB_PARSER)
    client: InnerTube = field(default=WEB_CLIENT)

    def __repr__(self) -> str:
        client_version: str = self.client.adaptor.context.client_version  # type: ignore

        return f"{type(self).__name__}({client_version!r})"

    def browse(self, browse_id: str) -> WebBrowseResponse:
        response: dict = self.client.adaptor.dispatch(
            "browse",
            body={"browseId": browse_id},
        )

        return self.parser.browse(response)

    def guide(self) -> WebGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)
