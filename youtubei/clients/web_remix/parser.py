from youtubei.parser import ClientParser

from .responses import (
    WebRemixConfigResponse,
    WebRemixGetBrowseAlbumDetailPageResponse,
    WebRemixGetBrowsePlaylistDetailPageResponse,
    WebRemixGuideResponse,
    WebRemixGetSearchResponse,
)

__all__ = ("WebRemixParser",)


class WebRemixParser(ClientParser):
    def browse_album(self, response, /) -> WebRemixGetBrowseAlbumDetailPageResponse:
        return self._parse(response, WebRemixGetBrowseAlbumDetailPageResponse)

    def browse_playlist(
        self, response, /
    ) -> WebRemixGetBrowsePlaylistDetailPageResponse:
        return self._parse(response, WebRemixGetBrowsePlaylistDetailPageResponse)

    def config(self, response, /) -> WebRemixConfigResponse:
        return self._parse(response, WebRemixConfigResponse)

    def guide(self, response, /) -> WebRemixGuideResponse:
        return self._parse(response, WebRemixGuideResponse)

    def search(self, response, /) -> WebRemixGetSearchResponse:
        return self._parse(response, WebRemixGetSearchResponse)
