from dataclasses import dataclass

from youtubei.registry import Registry

from .responses import IosGuideResponse


@dataclass
class IosParser:
    registry: Registry

    def parse_guide(self, response, /) -> IosGuideResponse:
        return IosGuideResponse.model_validate(
            response, context={"registry": self.registry}
        )
