from dataclasses import dataclass

from youtubei.registry import Registry
from youtubei.webremix.responses import WebRemixGuideResponse


@dataclass
class WebRemixParser:
    registry: Registry

    def parse_guide(self, response, /) -> WebRemixGuideResponse:
        return WebRemixGuideResponse.model_validate(response, context={"registry": self.registry})
