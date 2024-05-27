from typing import Sequence

from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.chip_cloud_chip import ChipCloudChipRenderer
from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("ChipCloudRenderer",)


@WEB_REMIX_REGISTRY
class ChipCloudRenderer(BaseRenderer):
    chips: Sequence[Dynamic[ChipCloudChipRenderer]]
    collapsed_row_count: int
    horizontal_scrollable: bool
