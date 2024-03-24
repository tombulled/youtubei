from typing import Sequence

from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.tab import TabRenderer

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class SingleColumnBrowseResultsRenderer(BaseRenderer):
    tabs: Sequence[Dynamic[TabRenderer]]
