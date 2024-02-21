from youtubei.models.other import AdTemplatedCountdown

from ._base import BaseRenderer


class AdDurationRemainingRenderer(BaseRenderer):
    templated_countdown: AdTemplatedCountdown
