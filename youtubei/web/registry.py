from typing import Final

from youtubei.registry import Registry
from youtubei import renderers

WEB_REGISTRY: Final[Registry] = Registry()

WEB_REGISTRY.add(renderers.ButtonRenderer)

WEB_REGISTRY.add(renderers.GuideEntryRenderer)
WEB_REGISTRY.add(renderers.GuideSectionRenderer)
WEB_REGISTRY.add(renderers.GuideSigninPromoRenderer)
