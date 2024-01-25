from enum import Enum


class _StrEnum(str, Enum):
    pass


class IconType(_StrEnum):
    # WEB_REMIX
    LIBRARY_MUSIC = "LIBRARY_MUSIC"
    TAB_EXPLORE = "TAB_EXPLORE"
    TAB_HOME = "TAB_HOME"
    ERROR_OUTLINE = "ERROR_OUTLINE"
    OPEN_IN_NEW = "OPEN_IN_NEW"
    INFO_OUTLINE = "INFO_OUTLINE"
    # WEB
    WHAT_TO_WATCH = "WHAT_TO_WATCH"
    TAB_SHORTS = "TAB_SHORTS"
    SUBSCRIPTIONS = "SUBSCRIPTIONS"
    HELP = "HELP"
    SETTINGS = "SETTINGS"
    VIDEO_LIBRARY_WHITE = "VIDEO_LIBRARY_WHITE"
    WATCH_HISTORY = "WATCH_HISTORY"
    YOUTUBE_ROUND = "YOUTUBE_ROUND"
    AVATAR_LOGGED_OUT = "AVATAR_LOGGED_OUT"
    TRENDING = "TRENDING"
    SHOPPING_BAG = "SHOPPING_BAG"
    MUSIC = "MUSIC"
    CLAPPERBOARD = "CLAPPERBOARD"
    LIVE = "LIVE"
    GAMING_LOGO = "GAMING_LOGO"
    NEWS = "NEWS"
    TROPHY = "TROPHY"
    COURSE = "COURSE"
    FASHION_LOGO = "FASHION_LOGO"
    BROADCAST = "BROADCAST"
    ADD_CIRCLE = "ADD_CIRCLE"
    UNPLUGGED_LOGO = "UNPLUGGED_LOGO"
    YOUTUBE_MUSIC = "YOUTUBE_MUSIC"
    YOUTUBE_KIDS_ROUND = "YOUTUBE_KIDS_ROUND"
    FLAG = "FLAG"
    FEEDBACK = "FEEDBACK"
    # IOS
    TAB_SUBSCRIPTIONS = "TAB_SUBSCRIPTIONS"
    TAB_ACTIVITY = "TAB_ACTIVITY"
    SEARCH = "SEARCH"
    ACCOUNT_CIRCLE = "ACCOUNT_CIRCLE"
    UNPLUGGED_RED_LOGO = "UNPLUGGED_RED_LOGO"
    MUSIC_RED_LOGO = "MUSIC_RED_LOGO"
    KIDS_RED_LOGO = "KIDS_RED_LOGO"
    YOUTUBE_LOGO = "YOUTUBE_LOGO"
    # IOS_MUSIC
    TAB_SAMPLES = "TAB_SAMPLES"


class Size(_StrEnum):
    DEFAULT: str = "SIZE_DEFAULT"


class Style(_StrEnum):
    BLUE_TEXT: str = "STYLE_BLUE_TEXT"
    DEFAULT: str = "STYLE_DEFAULT"
    PRIMARY: str = "STYLE_PRIMARY"
    SUGGESTIVE: str = "STYLE_SUGGESTIVE"
    TEXT: str = "STYLE_TEXT"
    UNKNOWN: str = "STYLE_UNKNOWN"


class Target(_StrEnum):
    NEW_WINDOW: str = "TARGET_NEW_WINDOW"


class WebPageType(_StrEnum):
    BROWSE: str = "WEB_PAGE_TYPE_BROWSE"
    CHANNEL: str = "WEB_PAGE_TYPE_CHANNEL"
    SETTINGS: str = "WEB_PAGE_TYPE_SETTINGS"
    SHORTS: str = "WEB_PAGE_TYPE_SHORTS"
    UNKNOWN: str = "WEB_PAGE_TYPE_UNKNOWN"
    WATCH: str = "WEB_PAGE_TYPE_WATCH"
