from typing import Final

from youtubei import renderers
from youtubei.parse import Registry

WEB_REMIX_REGISTRY: Final[Registry] = Registry()

WEB_REMIX_REGISTRY(renderers.ButtonRenderer)

WEB_REMIX_REGISTRY(renderers.GuideEntryRenderer)
WEB_REMIX_REGISTRY(renderers.GuideSectionRenderer)
WEB_REMIX_REGISTRY(renderers.GuideSigninPromoRenderer)
