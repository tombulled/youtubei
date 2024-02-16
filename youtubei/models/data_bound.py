from typing import Any, Union

from youtubei.models.endpoints import QueueAddEndpoint, WatchEndpoint
from youtubei.parse.validated_types import Dynamic

from .base import BaseModel


class DataBoundMenuItem(BaseModel):
    menu_item_renderer_mold: Dynamic[Any]  # MenuNavigationItemRenderer
    endpoint_mold: Dynamic[Any]


class DataBoundTopLevelMenuButton(BaseModel):
    menu_top_level_item_renderer_mold: Dynamic[Any]  # LikeButtonRenderer
