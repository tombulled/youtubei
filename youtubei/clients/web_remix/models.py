from youtubei.models._base import BaseModel
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.music_data_bound_menu import MusicDataBoundMenuRenderer

__all__ = (
    "MusicDisplayConfig",
    "MusicColdConfig",
    "MusicHotConfig",
    "RawColdConfigGroup",
    "RawHotConfigGroup",
    "GlobalConfigGroup",
)


class MusicDisplayConfig(BaseModel):
    track_context_menu: Dynamic[MusicDataBoundMenuRenderer]


class MusicColdConfig(BaseModel):
    enable_knight_rider: bool
    enable_short_stack: bool
    enable_bottom_sheet_account_switcher: bool
    enable_show_library: bool
    enable_remix_player_page: bool
    music_enable_home_page_disk_caching: bool
    ios_enable_lightweight_homepage: bool
    enable_show_download_in_library: bool
    android_enable_rx_for_player_events: bool
    enable_music_downloads_auto_offline: bool
    enable_woffle: bool


class MusicHotConfig(BaseModel):
    ios_enable_lightweight_collectionview: bool
    enable_offline_liked_tab: bool
    enable_restricted_mode_setting: bool
    enable_playback_logging: bool
    enable_android_shortcuts: bool
    prebuffer_content_length_ms: int
    prebuffer_countdown_time_ms: int
    enable_song_offline: bool
    enable_loop_on_missing_next_endpoint: bool
    enable_auto_opt_in_for_notifications: bool
    prefetch_max_retries: int
    prefetch_retry_interval_ms: int
    music_display_config: MusicDisplayConfig
    enable_network_change_snackbar: bool
    enable_ios_airplay_button: bool
    enable_media_browser_service: bool
    enable_restore_playback_state: bool
    enable_watch_history_notifier_conditional_renderer: bool
    enable_playback_queue: bool
    enable_innertube_search_suggestions_service: bool
    check_multiwindow_before_background: bool
    enable_quickseek_actions: bool
    enable_media_key_actions: bool
    enable_remix_offline_album_detail_page: bool
    enable_remix_downloads_section: bool
    enable_remix_offline_playlist_detail_page: bool
    music_enable_amplifier_in_watch_next_service: bool
    enable_media_browser_service_logging: bool
    music_enable_android_persistent_queue: bool


class RawColdConfigGroup(BaseModel):
    config_data: str
    music_cold_config: MusicColdConfig


class RawHotConfigGroup(BaseModel):
    music_hot_config: MusicHotConfig


class GlobalConfigGroup(BaseModel):
    hot_hash_data: str
    cold_hash_data: str
    raw_cold_config_group: RawColdConfigGroup
    raw_hot_config_group: RawHotConfigGroup
