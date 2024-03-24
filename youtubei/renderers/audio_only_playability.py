from youtubei.enums import FeatureAvailability

from ._base import BaseRenderer

__all__ = ("AudioOnlyPlayabilityRenderer",)


class AudioOnlyPlayabilityRenderer(BaseRenderer):
    audio_only_availability: FeatureAvailability
