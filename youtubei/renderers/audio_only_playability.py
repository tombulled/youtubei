from youtubei.enums import FeatureAvailability
from ._base import BaseRenderer


class AudioOnlyPlayabilityRenderer(BaseRenderer):
    audio_only_availability: FeatureAvailability
