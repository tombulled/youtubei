from youtubei.abc import ClientParser

from .responses import WebRemixGuideResponse

__all__ = ("WebRemixParser",)


class WebRemixParser(ClientParser):
    def guide(self, response, /) -> WebRemixGuideResponse:
        return self._parse(response, WebRemixGuideResponse)
