from youtubei.parser import ClientParser

from .responses import WebBrowseResponse, WebGuideResponse

__all__ = ("WebParser",)


class WebParser(ClientParser):
    def browse(self, response, /) -> WebBrowseResponse:
        return self._parse(response, WebBrowseResponse)

    def guide(self, response, /) -> WebGuideResponse:
        return self._parse(response, WebGuideResponse)
