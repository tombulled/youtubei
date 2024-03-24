from typing import Sequence
from youtubei.parse.validated_types import Dynamic

from youtubei.renderers.tab import TabRenderer
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class SingleColumnBrowseResultsRenderer(BaseRenderer):
    tabs: Sequence[Dynamic[TabRenderer]]
