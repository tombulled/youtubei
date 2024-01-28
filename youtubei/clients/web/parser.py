from dataclasses import dataclass

from youtubei.registry import Registry

from .responses import WebGuideResponse


@dataclass
class WebParser:
    registry: Registry

    def parse_guide(self, response, /) -> WebGuideResponse:
        return WebGuideResponse.model_validate(
            response, context={"registry": self.registry}
        )
