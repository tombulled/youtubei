from typing import Any, Sequence

from youtubei._registries import WEB_REGISTRY
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.playlist_sidebar_primary_info import (
    PlaylistSidebarPrimaryInfoRenderer,
)

from ._base import BaseRenderer

__all__ = ("PlaylistSidebarRenderer",)


@WEB_REGISTRY
class PlaylistSidebarRenderer(BaseRenderer):
    items: Sequence[Dynamic[PlaylistSidebarPrimaryInfoRenderer]]
