from ._base import BaseRenderer

__all__ = ("AdBreakServiceRenderer",)


class AdBreakServiceRenderer(BaseRenderer):
    prefetch_milliseconds: str
    get_ad_break_url: str
