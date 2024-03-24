from typing import Sequence

from youtubei.models.other import AudioTrack, CaptionTrack, TranslationLanguage

from ._base import BaseRenderer

__all__ = ("PlayerCaptionsTracklistRenderer",)


class PlayerCaptionsTracklistRenderer(BaseRenderer):
    caption_tracks: Sequence[CaptionTrack]
    audio_tracks: Sequence[AudioTrack]
    translation_languages: Sequence[TranslationLanguage]
    default_audio_track_index: int
