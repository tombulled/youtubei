from youtubei.parser import ClientParser

from .responses import IosMusicGuideResponse

__all__ = ("IosMusicParser",)


class IosMusicParser(ClientParser):
    def guide(self, response, /) -> IosMusicGuideResponse:
        return self._parse(response, IosMusicGuideResponse)
