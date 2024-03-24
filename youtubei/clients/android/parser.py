from youtubei.parser import ClientParser

from .responses import AndroidGuideResponse

__all__ = ("AndroidParser",)


class AndroidParser(ClientParser):
    def guide(self, response, /) -> AndroidGuideResponse:
        return self._parse(response, AndroidGuideResponse)
