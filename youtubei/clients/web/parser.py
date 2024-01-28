from youtubei.abc import ClientParser

from .responses import WebGuideResponse

__all__ = ("WebParser",)


class WebParser(ClientParser):
    def guide(self, response, /) -> WebGuideResponse:
        return self._parse(response, WebGuideResponse)
