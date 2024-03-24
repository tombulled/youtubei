from youtubei.models.other import AdTemplatedCountdown

from ._base import BaseRenderer

__all__ = ("AdDurationRemainingRenderer",)


class AdDurationRemainingRenderer(BaseRenderer):
    templated_countdown: AdTemplatedCountdown
