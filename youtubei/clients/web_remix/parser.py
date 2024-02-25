from youtubei.abc import ClientParser

from .responses import (
    WebRemixBrowseResponse,
    WebRemixConfigResponse,
    WebRemixGuideResponse,
)

__all__ = ("WebRemixParser",)


class WebRemixParser(ClientParser):
    def browse(self, response, /) -> WebRemixBrowseResponse:
        return self._parse(response, WebRemixBrowseResponse)

    def config(self, response, /) -> WebRemixConfigResponse:
        return self._parse(response, WebRemixConfigResponse)

    def guide(self, response, /) -> WebRemixGuideResponse:
        return self._parse(response, WebRemixGuideResponse)
