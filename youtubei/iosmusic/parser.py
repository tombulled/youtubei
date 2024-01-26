from dataclasses import dataclass

from youtubei.registry import Registry

from .responses import IosMusicGuideResponse


@dataclass
class IosMusicParser:
    registry: Registry

    def parse_guide(self, response, /) -> IosMusicGuideResponse:
        return IosMusicGuideResponse.model_validate(
            response, context={"registry": self.registry}
        )
