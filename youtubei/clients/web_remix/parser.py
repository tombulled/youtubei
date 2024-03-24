from youtubei.abc import ClientParser

from .responses import (
    WebRemixConfigResponse,
    WebRemixGetBrowseAlbumDetailPageResponse,
    WebRemixGetBrowsePlaylistDetailPageResponse,
    WebRemixGuideResponse,
)

__all__ = ("WebRemixParser",)


class WebRemixParser(ClientParser):
    def browse_album(self, response, /) -> WebRemixGetBrowseAlbumDetailPageResponse:
        return self._parse(response, WebRemixGetBrowseAlbumDetailPageResponse)
    
    def browse_playlist(self, response, /) -> WebRemixGetBrowsePlaylistDetailPageResponse:
        return self._parse(response, WebRemixGetBrowsePlaylistDetailPageResponse)

    def config(self, response, /) -> WebRemixConfigResponse:
        return self._parse(response, WebRemixConfigResponse)

    def guide(self, response, /) -> WebRemixGuideResponse:
        return self._parse(response, WebRemixGuideResponse)
