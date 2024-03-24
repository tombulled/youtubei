from typing import Any

from youtubei.parse.validated_types import Dynamic

from ._base import BaseModel

__all__ = (
    "DataBoundMenuItem",
    "DataBoundTopLevelMenuButton",
)


class DataBoundMenuItem(BaseModel):
    menu_item_renderer_mold: Dynamic[Any]  # Observed: MenuNavigationItemRenderer
    endpoint_mold: Dynamic[Any]


class DataBoundTopLevelMenuButton(BaseModel):
    menu_top_level_item_renderer_mold: Dynamic[Any]  # Observed: LikeButtonRenderer
