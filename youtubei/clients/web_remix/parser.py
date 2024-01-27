from youtubei.abc import ClientParser

from .responses import WebRemixGuideResponse


class WebRemixParser(ClientParser):
    def guide(self, response, /) -> WebRemixGuideResponse:
        return self._parse(response, WebRemixGuideResponse)
