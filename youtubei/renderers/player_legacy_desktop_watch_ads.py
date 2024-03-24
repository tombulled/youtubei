from youtubei.models.params import GutParams, PlayerAdParams

from ._base import BaseRenderer

__all__ = ("PlayerLegacyDesktopWatchAdsRenderer",)


class PlayerLegacyDesktopWatchAdsRenderer(BaseRenderer):
    playerAdParams: PlayerAdParams
    gut_params: GutParams
    show_companion: bool
    show_instream: bool
    use_gut: bool
