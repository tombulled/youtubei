from dataclasses import dataclass

from youtubei.registry import Registry

from .responses import AndroidGuideResponse


@dataclass
class AndroidParser:
    registry: Registry

    def parse_guide(self, response, /) -> AndroidGuideResponse:
        return AndroidGuideResponse.model_validate(
            response, context={"registry": self.registry}
        )
