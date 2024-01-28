from typing import Sequence, Union

from typing_extensions import TypeAlias

from youtubei._registries import IOS_REGISTRY
from youtubei.parse import Dynamic
from youtubei.renderers.background_promo import BackgroundPromoRenderer
from youtubei.renderers.compact_link import CompactLinkRenderer

from ._base import BaseRenderer
from youtubei._registries import ANDROID_REGISTRY

MultiPageMenuSectionItem: TypeAlias = Dynamic[
    Union[
        BackgroundPromoRenderer,
        CompactLinkRenderer,
    ]
]


@ANDROID_REGISTRY
@IOS_REGISTRY
class MultiPageMenuSectionRenderer(BaseRenderer):
    items: Sequence[MultiPageMenuSectionItem]
