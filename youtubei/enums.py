from enum import Enum, auto


class StrEnum(str, Enum):
    pass


# E.g., {"guideEntryRenderer": {"targetId": "library-guide-item"}}
# Note: unsure whether this should be an enum or just a str
class TargetId(StrEnum):
    # YouTube Web
    LIBRARY_GUIDE_ITEM = "library-guide-item"
    # YouTube iOS
    PIVOT_W2W = "pivot-w2w"
    PIVOT_EXPLORE = "pivot-explore"
    PIVOT_SUBS = "pivot-subs"
    PIVOT_LIBRARY = "pivot-library"
    TOPBAR_NOTIFICATIONS = "topbar-notifications"
    TOPBAR_USER_AVATAR = "topbar-user-avatar"
    # YouTubeMusic iOS
    NONE = ""
    PIVOT_MUSIC_IMMERSIVE = "pivot-music-immersive"
    PIVOT_MUSIC_EXPLORE = "pivot-music-explore"
    PIVOT_MUSIC_LIBRARY = "pivot-music-library"


# E.g., {"urlEndpoint": {"target": "TARGET_NEW_WINDOW"}}
class Target(StrEnum):
    NEW_WINDOW: str = "TARGET_NEW_WINDOW"


class ButtonStyle(StrEnum):
    DEFAULT: str = "STYLE_DEFAULT"
    SUGGESTIVE: str = "STYLE_SUGGESTIVE"
    PRIMARY: str = "STYLE_PRIMARY"


class ButtonSize(StrEnum):
    DEFAULT: str = "SIZE_DEFAULT"


# A "service" as listed under "responseContext.serviceTrackingParams"
class Service(StrEnum):
    CSI: str = "CSI"
    GFEEDBACK: str = "GFEEDBACK"
    ECATCHER: str = "ECATCHER"


# E.g., {"icon": {"iconType": "TAB_HOME"}}
class IconType(StrEnum):
    # YouTube Music
    LIBRARY_MUSIC = "LIBRARY_MUSIC"
    TAB_EXPLORE = "TAB_EXPLORE"
    TAB_HOME = "TAB_HOME"
    # YouTube Web
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
    # YouTube iOS
    TAB_SUBSCRIPTIONS = "TAB_SUBSCRIPTIONS"
    TAB_ACTIVITY = "TAB_ACTIVITY"
    SEARCH = "SEARCH"
    ACCOUNT_CIRCLE = "ACCOUNT_CIRCLE"
    UNPLUGGED_RED_LOGO = "UNPLUGGED_RED_LOGO"
    MUSIC_RED_LOGO = "MUSIC_RED_LOGO"
    KIDS_RED_LOGO = "KIDS_RED_LOGO"
    YOUTUBE_LOGO = "YOUTUBE_LOGO"
    # YouTube Music iOS
    TAB_SAMPLES = "TAB_SAMPLES"


class SharePanelType(Enum):
    SHARE_PANEL_TYPE_UNIFIED_SHARE_PANEL = auto()


# E.g., {"browseEndpointContextMusicConfig": {"pageType": "MUSIC_PAGE_TYPE_METRONOME"}}
class MusicPageType(StrEnum):
    METRONOME = "MUSIC_PAGE_TYPE_METRONOME"


# E.g., {"webCommandMetadata": {"webPageType": "WEB_PAGE_TYPE_BROWSE"}}
class WebPageType(StrEnum):
    BROWSE: str = "WEB_PAGE_TYPE_BROWSE"
    CHANNEL: str = "WEB_PAGE_TYPE_CHANNEL"
    SHORTS: str = "WEB_PAGE_TYPE_SHORTS"
    UNKNOWN: str = "WEB_PAGE_TYPE_UNKNOWN"
    SETTINGS: str = "WEB_PAGE_TYPE_SETTINGS"


# E.g., {"signalServiceEndpoint": {"signal": "CLIENT_SIGNAL"}}
class SignalServiceSignal(StrEnum):
    CLIENT_SIGNAL: str = "CLIENT_SIGNAL"


# E.g., {"signalAction": {"signal": "HELP"}}
class SignalActionSignal(StrEnum):
    HELP: str = "HELP"


# E.g., {"reelWatchEndpoint": {"sequenceProvider": "REEL_WATCH_SEQUENCE_PROVIDER_RPC"}}
class ReelWatchSequenceProvider(StrEnum):
    RPC: str = "REEL_WATCH_SEQUENCE_PROVIDER_RPC"


# E.g., {"reelWatchEndpoint": {"inputType": "REEL_WATCH_INPUT_TYPE_SEEDLESS"}}
class ReelWatchInputType(StrEnum):
    SEEDLESS: str = "REEL_WATCH_INPUT_TYPE_SEEDLESS"


# E.g., {"reelPlayerOverlayRenderer": {"style": "REEL_PLAYER_OVERLAY_STYLE_SHORTS"}}
class ReelPlayerOverlayStyle(StrEnum):
    SHORTS: str = "REEL_PLAYER_OVERLAY_STYLE_SHORTS"


# E.g., {"reelPlayerOverlayRenderer": {"reelPlayerNavigationModel": "REEL_PLAYER_NAVIGATION_MODEL_UNSPECIFIED"}}
class ReelPlayerNavigationModel(StrEnum):
    UNSPECIFIED: str = "REEL_PLAYER_NAVIGATION_MODEL_UNSPECIFIED"


# E.g., {"backgroundPromoRenderer": {"style": {"value": "BACKGROUND_PROMO_STYLE_TYPE_EMPTY_STATE"}}}
class BackgroundPromoStyleType(StrEnum):
    EMPTY_STATE = "BACKGROUND_PROMO_STYLE_TYPE_EMPTY_STATE"
