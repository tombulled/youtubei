from ._base import StrEnum

__all__ = (
    "MusicItemThumbnailOverlayContentPosition",
    "MusicItemThumbnailOverlayDisplayStyle",
    "MusicPlayButtonRippleTarget",
    "MusicPlayButtonSize",
    "MusicResponsiveListItemColumnDisplayPriority",
    "MusicResponsiveListItemFixedColumnSize",
    "MusicResponsiveListItemHeight",
    "MusicResponsiveListItemFlexColumnDisplayStyle",
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
    TALL: str = "MUSIC_RESPONSIVE_LIST_ITEM_HEIGHT_TALL"


class MusicResponsiveListItemFlexColumnDisplayStyle(StrEnum):
    TWO_LINE_STACK: str = (
        "MUSIC_RESPONSIVE_LIST_ITEM_FLEX_COLUMN_DISPLAY_STYLE_TWO_LINE_STACK"
    )


class MusicThumbnailCrop(StrEnum):
    UNSPECIFIED: str = "MUSIC_THUMBNAIL_CROP_UNSPECIFIED"
    CIRCLE: str = "MUSIC_THUMBNAIL_CROP_CIRCLE"


class MusicThumbnailScale(StrEnum):
    ASPECT_FIT: str = "MUSIC_THUMBNAIL_SCALE_ASPECT_FIT"
    ASPECT_FILL: str = "MUSIC_THUMBNAIL_SCALE_ASPECT_FILL"
    UNSPECIFIED: str = "MUSIC_THUMBNAIL_SCALE_UNSPECIFIED"


class MusicVideoType(StrEnum):
    ATV: str = "MUSIC_VIDEO_TYPE_ATV"
    OMV: str = "MUSIC_VIDEO_TYPE_OMV"
    UGC: str = "MUSIC_VIDEO_TYPE_UGC"
    PODCAST_EPISODE: str = "MUSIC_VIDEO_TYPE_PODCAST_EPISODE"
