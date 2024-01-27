from typing import Final

from youtubei import renderers
from youtubei.models.reminders import DataReminder
from youtubei.registry import Registry

ANDROID_REGISTRY: Final[Registry] = Registry()

# Models
ANDROID_REGISTRY.add(DataReminder)

# Renderers
ANDROID_REGISTRY.add(renderers.BackgroundPromoRenderer)
ANDROID_REGISTRY.add(renderers.ButtonRenderer)
ANDROID_REGISTRY.add(renderers.CompactLinkRenderer)
ANDROID_REGISTRY.add(renderers.ConfirmDialogRenderer)
ANDROID_REGISTRY.add(renderers.EngagementPanelSectionListRenderer)
ANDROID_REGISTRY.add(renderers.EngagementPanelTitleHeaderRenderer)
ANDROID_REGISTRY.add(renderers.ItemSectionRenderer)
ANDROID_REGISTRY.add(renderers.LugashFooterRenderer)
ANDROID_REGISTRY.add(renderers.MobileTopbarRenderer)
ANDROID_REGISTRY.add(renderers.MultiPageMenuRenderer)
ANDROID_REGISTRY.add(renderers.MultiPageMenuSectionRenderer)
ANDROID_REGISTRY.add(renderers.PivotBarRenderer)
ANDROID_REGISTRY.add(renderers.PivotBarItemRenderer)
ANDROID_REGISTRY.add(renderers.PrivacyTosFooterRenderer)
ANDROID_REGISTRY.add(renderers.SectionListRenderer)
ANDROID_REGISTRY.add(renderers.TopbarButtonRenderer)
ANDROID_REGISTRY.add(renderers.TopbarLogoRenderer)
ANDROID_REGISTRY.add(renderers.TopbarMenuButtonRenderer)
ANDROID_REGISTRY.add(renderers.WatchBreakRenderer)
