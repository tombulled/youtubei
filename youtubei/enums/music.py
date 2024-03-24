from ._base import StrEnum

__all__ = (
    "MusicItemThumbnailOverlayContentPosition",
    "MusicItemThumbnailOverlayDisplayStyle",
    "MusicPlayButtonRippleTarget",
    "MusicPlayButtonSize",
    "MusicResponsiveListItemColumnDisplayPriority",
    "MusicResponsiveListItemFixedColumnSize",
    "MusicResponsiveListItemHeight",
    "MusicThumbnailCrop",
    "MusicThumbnailScale",
    "MusicVideoType",
)


class MusicItemThumbnailOverlayContentPosition(StrEnum):
    CENTERED: str = "MUSIC_ITEM_THUMBNAIL_OVERLAY_CONTENT_POSITION_CENTERED"


class MusicItemThumbnailOverlayDisplayStyle(StrEnum):
    PERSISTENT: str = "MUSIC_ITEM_THUMBNAIL_OVERLAY_DISPLAY_STYLE_PERSISTENT"


class MusicPlayButtonRippleTarget(StrEnum):
    SELF: str = "MUSIC_PLAY_BUTTON_RIPPLE_TARGET_SELF"


class MusicPlayButtonSize(StrEnum):
    SMALL: str = "MUSIC_PLAY_BUTTON_SIZE_SMALL"


class MusicResponsiveListItemColumnDisplayPriority(StrEnum):
    HIGH: str = "MUSIC_RESPONSIVE_LIST_ITEM_COLUMN_DISPLAY_PRIORITY_HIGH"
    MEDIUM: str = "MUSIC_RESPONSIVE_LIST_ITEM_COLUMN_DISPLAY_PRIORITY_MEDIUM"


class MusicResponsiveListItemFixedColumnSize(StrEnum):
    SMALL: str = "MUSIC_RESPONSIVE_LIST_ITEM_FIXED_COLUMN_SIZE_SMALL"


class MusicResponsiveListItemHeight(StrEnum):
    MEDIUM: str = "MUSIC_RESPONSIVE_LIST_ITEM_HEIGHT_MEDIUM"


class MusicThumbnailCrop(StrEnum):
    UNSPECIFIED: str = "MUSIC_THUMBNAIL_CROP_UNSPECIFIED"


class MusicThumbnailScale(StrEnum):
    ASPECT_FIT: str = "MUSIC_THUMBNAIL_SCALE_ASPECT_FIT"
    UNSPECIFIED: str = "MUSIC_THUMBNAIL_SCALE_UNSPECIFIED"


class MusicVideoType(StrEnum):
    ATV: str = "MUSIC_VIDEO_TYPE_ATV"
    OMV: str = "MUSIC_VIDEO_TYPE_OMV"
