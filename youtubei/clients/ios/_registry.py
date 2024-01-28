from typing import Final

from youtubei import renderers
from youtubei.registry import Registry

IOS_REGISTRY: Final[Registry] = Registry()

IOS_REGISTRY.add(renderers.BackgroundPromoRenderer)

IOS_REGISTRY.add(renderers.ButtonRenderer)

IOS_REGISTRY.add(renderers.CompactLinkRenderer)

IOS_REGISTRY.add(renderers.LugashFooterRenderer)

IOS_REGISTRY.add(renderers.MobileTopbarRenderer)

IOS_REGISTRY.add(renderers.MultiPageMenuSectionRenderer)
IOS_REGISTRY.add(renderers.MultiPageMenuRenderer)

IOS_REGISTRY.add(renderers.PivotBarItemRenderer)
IOS_REGISTRY.add(renderers.PivotBarRenderer)

IOS_REGISTRY.add(renderers.PrivacyTosFooterRenderer)

IOS_REGISTRY.add(renderers.UploadProgressArrowRenderer)

IOS_REGISTRY.add(renderers.TopbarButtonRenderer)
IOS_REGISTRY.add(renderers.TopbarLogoRenderer)
IOS_REGISTRY.add(renderers.TopbarMenuButtonRenderer)
