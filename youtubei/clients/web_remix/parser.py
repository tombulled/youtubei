from youtubei.abc import ClientParser

from .responses import WebRemixConfigResponse, WebRemixGuideResponse

__all__ = ("WebRemixParser",)


class WebRemixParser(ClientParser):
    def config(self, response, /) -> WebRemixConfigResponse:
        return self._parse(response, WebRemixConfigResponse)

    def guide(self, response, /) -> WebRemixGuideResponse:
        return self._parse(response, WebRemixGuideResponse)
