from typing import Sequence
from youtubei._registries import WEB_REMIX_REGISTRY
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.tab import TabRenderer

from ._base import BaseRenderer

__all__ = ("TabbedSearchResultsRenderer",)


@WEB_REMIX_REGISTRY
class TabbedSearchResultsRenderer(BaseRenderer):
    tabs: Sequence[Dynamic[TabRenderer]]
