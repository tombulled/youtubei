from typing import Final

from youtubei.registry import Registry
from youtubei.renderers.button import ButtonRenderer
from youtubei.renderers.guide import GuideEntryRenderer, GuideSectionRenderer, GuideSigninPromoRenderer

WEB_REMIX_REGISTRY: Final[Registry] = Registry()

WEB_REMIX_REGISTRY.add(ButtonRenderer)

WEB_REMIX_REGISTRY.add(GuideEntryRenderer)
WEB_REMIX_REGISTRY.add(GuideSectionRenderer)
WEB_REMIX_REGISTRY.add(GuideSigninPromoRenderer)
