from typing import Final

from youtubei import renderers
from youtubei.registry import Registry

WEB_REMIX_REGISTRY: Final[Registry] = Registry()

WEB_REMIX_REGISTRY.add(renderers.ButtonRenderer)

WEB_REMIX_REGISTRY.add(renderers.GuideEntryRenderer)
WEB_REMIX_REGISTRY.add(renderers.GuideSectionRenderer)
WEB_REMIX_REGISTRY.add(renderers.GuideSigninPromoRenderer)
