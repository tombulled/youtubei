from ._other import _StrEnum


class MusicThumbnailCrop(_StrEnum):
    UNSPECIFIED: str = "MUSIC_THUMBNAIL_CROP_UNSPECIFIED"


class MusicThumbnailScale(_StrEnum):
    ASPECT_FIT: str = "MUSIC_THUMBNAIL_SCALE_ASPECT_FIT"


class MusicItemThumbnailOverlayContentPosition(_StrEnum):
    CENTERED: str = "MUSIC_ITEM_THUMBNAIL_OVERLAY_CONTENT_POSITION_CENTERED"


class MusicItemThumbnailOverlayDisplayStyle(_StrEnum):
    PERSISTENT: str = "MUSIC_ITEM_THUMBNAIL_OVERLAY_DISPLAY_STYLE_PERSISTENT"


class MusicPlayButtonSize(_StrEnum):
    SMALL: str = "MUSIC_PLAY_BUTTON_SIZE_SMALL"


class MusicPlayButtonRippleTarget(_StrEnum):
    SELF: str = "MUSIC_PLAY_BUTTON_RIPPLE_TARGET_SELF"


class MusicResponsiveListItemColumnDisplayPriority(_StrEnum):
    HIGH: str = "MUSIC_RESPONSIVE_LIST_ITEM_COLUMN_DISPLAY_PRIORITY_HIGH"
    MEDIUM: str = "MUSIC_RESPONSIVE_LIST_ITEM_COLUMN_DISPLAY_PRIORITY_MEDIUM"


class MusicResponsiveListItemFixedColumnSize(_StrEnum):
    SMALL: str = "MUSIC_RESPONSIVE_LIST_ITEM_FIXED_COLUMN_SIZE_SMALL"


class MusicVideoType(_StrEnum):
    ATV: str = "MUSIC_VIDEO_TYPE_ATV"
