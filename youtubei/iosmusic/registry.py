from typing import Final

from youtubei import renderers
from youtubei.registry import Registry

IOS_MUSIC_REGISTRY: Final[Registry] = Registry()

IOS_MUSIC_REGISTRY.add(renderers.PivotBarItemRenderer)
IOS_MUSIC_REGISTRY.add(renderers.PivotBarRenderer)
