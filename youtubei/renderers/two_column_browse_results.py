from typing import Sequence

from youtubei._registries import WEB_REMIX_REGISTRY, WEB_REGISTRY
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.tab import TabRenderer

from ._base import BaseRenderer

@WEB_REMIX_REGISTRY
@WEB_REGISTRY
class TwoColumnBrowseResultsRenderer(BaseRenderer):
    tabs: Sequence[Dynamic[TabRenderer]]
