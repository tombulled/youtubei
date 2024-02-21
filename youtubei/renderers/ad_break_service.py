from ._base import BaseRenderer


class AdBreakServiceRenderer(BaseRenderer):
    prefetch_milliseconds: str
    get_ad_break_url: str
