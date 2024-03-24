from typing import Any, Optional

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.other import Icon
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("MenuNavigationItemRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class MenuNavigationItemRenderer(BaseRenderer):
    text: Text  # Observed: ComplexText, SimpleText
    icon: Icon
    navigation_endpoint: Optional[
        DynamicCommand[
            Any
            # Observed: ModalEndpoint, WatchEndpoint, BrowseEndpoint, ShareEntityEndpoint, WatchPlaylistEndpoint
        ]
    ] = None
