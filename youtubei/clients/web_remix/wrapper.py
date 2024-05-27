from dataclasses import dataclass, field
from typing import Optional

from innertube import InnerTube, utils
from innertube.enums import Endpoint

from .constants import WEB_REMIX_CLIENT, WEB_REMIX_PARSER
from .parser import WebRemixParser
from .responses import (
    WebRemixConfigResponse,
    WebRemixGetBrowseAlbumDetailPageResponse,
    WebRemixGetBrowsePlaylistDetailPageResponse,
    WebRemixGuideResponse,
)

__all__ = ("WebRemix",)


@dataclass
class WebRemix:
    parser: WebRemixParser = field(default=WEB_REMIX_PARSER)
    client: InnerTube = field(default=WEB_REMIX_CLIENT)

    def __repr__(self) -> str:
        client_version: str = self.client.adaptor.context.client_version  # type: ignore

        return f"{type(self).__name__}({client_version!r})"

    def _browse(self, browse_id: str, /) -> dict:
        return self.client.adaptor.dispatch(
            "browse",
            body={"browseId": browse_id},
        )

    def browse_album(
        self, browse_id: str, /
    ) -> WebRemixGetBrowseAlbumDetailPageResponse:
        response: dict = self._browse(browse_id)

        return self.parser.browse_album(response)

    def browse_playlist(
        self, browse_id: str, /
    ) -> WebRemixGetBrowsePlaylistDetailPageResponse:
        response: dict = self._browse(browse_id)

        return self.parser.browse_playlist(response)

    def config(self) -> WebRemixConfigResponse:
        response: dict = self.client.adaptor.dispatch("config")

        return self.parser.config(response)

    def guide(self) -> WebRemixGuideResponse:
        response: dict = self.client.adaptor.dispatch("guide")

        return self.parser.guide(response)

    def search(
        self,
        query: Optional[str] = None,
        *,
        params: Optional[str] = None,
        continuation: Optional[str] = None,
    ):
        response: dict = self.client.adaptor.dispatch(
            Endpoint.SEARCH,
            body=utils.filter(
                dict(
                    query=query or "",
                    params=params,
                    continuation=continuation,
                )
            ),
        )

        return self.parser.search(response)
