from youtubei.parser import ClientParser

from .responses import IosGuideResponse

__all__ = ("IosParser",)


class IosParser(ClientParser):
    def guide(self, response, /) -> IosGuideResponse:
        return self._parse(response, IosGuideResponse)
