from enum import Enum

__all__ = (
    "BackgroundPromoStyleType",
    "IconType",
    "MusicPageType",
    "PlaybackMode",
    "ReelPlayerNavigationModel",
    "ReelPlayerOverlayStyle",
    "ReelWatchInputType",
    "ReelWatchSequenceProvider",
    "Service",
    "SharePanelType",
    "SignalActionSignal",
    "SignalServiceSignal",
    "Size",
    "Style",
    "Target",
    "TargetId",
    "WebPageType",
)


class _StrEnum(str, Enum):
    pass


# E.g., {"backgroundPromoRenderer": {"style": {"value": "BACKGROUND_PROMO_STYLE_TYPE_EMPTY_STATE"}}}
class BackgroundPromoStyleType(_StrEnum):
    EMPTY_STATE = "BACKGROUND_PROMO_STYLE_TYPE_EMPTY_STATE"


class CaptionsInitialState(_StrEnum):
    OFF_RECOMMENDED = "CAPTIONS_INITIAL_STATE_OFF_RECOMMENDED"


# E.g., {"icon": {"iconType": "TAB_HOME"}}
class IconType(_StrEnum):
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


class LanguageCode(_StrEnum):
    AF = "af"  # Afrikaans
    AK = "ak"  # Akan
    SQ = "sq"  # Albanian
    AM = "am"  # Amharic
    AR = "ar"  # Arabic
    HY = "hy"  # Armenian
    AS = "as"  # Assamese
    AY = "ay"  # Aymara
    AZ = "az"  # Azerbaijani
    BN = "bn"  # Bangla
    EU = "eu"  # Basque
    BE = "be"  # Belarusian
    BHO = "bho"  # Bhojpuri
    BS = "bs"  # Bosnian
    BG = "bg"  # Bulgarian
    MY = "my"  # Burmese
    CA = "ca"  # Catalan
    CEB = "ceb"  # Cebuano
    ZH_HANS = "zh-Hans"  # Chinese (Simplified)
    ZH_HANT = "zh-Hant"  # Chinese (Traditional)
    CO = "co"  # Corsican
    HR = "hr"  # Croatian
    CS = "cs"  # Czech
    DA = "da"  # Danish
    DV = "dv"  # Divehi
    NL = "nl"  # Dutch
    EN = "en"  # English
    EO = "eo"  # Esperanto
    ET = "et"  # Estonian
    EE = "ee"  # Ewe
    FIL = "fil"  # Filipino
    FI = "fi"  # Finnish
    FR = "fr"  # French
    GL = "gl"  # Galician
    LG = "lg"  # Ganda
    KA = "ka"  # Georgian
    DE = "de"  # German
    EL = "el"  # Greek
    GN = "gn"  # Guarani
    GU = "gu"  # Gujarati
    HT = "ht"  # Haitian Creole
    HA = "ha"  # Hausa
    HAW = "haw"  # Hawaiian
    IW = "iw"  # Hebrew
    HI = "hi"  # Hindi
    HMN = "hmn"  # Hmong
    HU = "hu"  # Hungarian
    IS = "is"  # Icelandic
    IG = "ig"  # Igbo
    ID = "id"  # Indonesian
    GA = "ga"  # Irish
    IT = "it"  # Italian
    JA = "ja"  # Japanese
    JV = "jv"  # Javanese
    KN = "kn"  # Kannada
    KK = "kk"  # Kazakh
    KM = "km"  # Khmer
    RW = "rw"  # Kinyarwanda
    KO = "ko"  # Korean
    KRI = "kri"  # Krio
    KU = "ku"  # Kurdish
    KY = "ky"  # Kyrgyz
    LO = "lo"  # Lao
    LA = "la"  # Latin
    LV = "lv"  # Latvian
    LN = "ln"  # Lingala
    LT = "lt"  # Lithuanian
    LB = "lb"  # Luxembourgish
    MK = "mk"  # Macedonian
    MG = "mg"  # Malagasy
    MS = "ms"  # Malay
    ML = "ml"  # Malayalam
    MT = "mt"  # Maltese
    MI = "mi"  # Māori
    MR = "mr"  # Marathi
    MN = "mn"  # Mongolian
    NE = "ne"  # Nepali
    NSO = "nso"  # Northern Sotho
    NO = "no"  # Norwegian
    NY = "ny"  # Nyanja
    OR = "or"  # Odia
    OM = "om"  # Oromo
    PS = "ps"  # Pashto
    FA = "fa"  # Persian
    PL = "pl"  # Polish
    PT = "pt"  # Portuguese
    PA = "pa"  # Punjabi
    QU = "qu"  # Quechua
    RO = "ro"  # Romanian
    RU = "ru"  # Russian
    SM = "sm"  # Samoan
    SA = "sa"  # Sanskrit
    GD = "gd"  # Scottish Gaelic
    SR = "sr"  # Serbian
    SN = "sn"  # Shona
    SD = "sd"  # Sindhi
    SI = "si"  # Sinhala
    SK = "sk"  # Slovak
    SL = "sl"  # Slovenian
    SO = "so"  # Somali
    ST = "st"  # Southern Sotho
    ES = "es"  # Spanish
    SU = "su"  # Sundanese
    SW = "sw"  # Swahili
    SV = "sv"  # Swedish
    TG = "tg"  # Tajik
    TA = "ta"  # Tamil
    TT = "tt"  # Tatar
    TE = "te"  # Telugu
    TH = "th"  # Thai
    TI = "ti"  # Tigrinya
    TS = "ts"  # Tsonga
    TR = "tr"  # Turkish
    TK = "tk"  # Turkmen
    UK = "uk"  # Ukrainian
    UR = "ur"  # Urdu
    UG = "ug"  # Uyghur
    UZ = "uz"  # Uzbek
    VI = "vi"  # Vietnamese
    CY = "cy"  # Welsh
    FY = "fy"  # Western Frisian
    XH = "xh"  # Xhosa
    YI = "yi"  # Yiddish
    YO = "yo"  # Yoruba
    ZU = "zu"  # Zulu


# E.g., {"browseEndpointContextMusicConfig": {"pageType": "MUSIC_PAGE_TYPE_METRONOME"}}
class MusicPageType(_StrEnum):
    METRONOME = "MUSIC_PAGE_TYPE_METRONOME"


# E.g. {'miniplayerRenderer': {'playbackMode': 'PLAYBACK_MODE_ALLOW'}}
class PlaybackMode(_StrEnum):
    ALLOW = "PLAYBACK_MODE_ALLOW"


# E.g., {"openPopupAction": {"type": "DIALOG"}}
class PopupType(_StrEnum):
    DIALOG = "DIALOG"


# E.g., {"reelPlayerOverlayRenderer": {"reelPlayerNavigationModel": "REEL_PLAYER_NAVIGATION_MODEL_UNSPECIFIED"}}
class ReelPlayerNavigationModel(_StrEnum):
    UNSPECIFIED: str = "REEL_PLAYER_NAVIGATION_MODEL_UNSPECIFIED"


# E.g., {"reelPlayerOverlayRenderer": {"style": "REEL_PLAYER_OVERLAY_STYLE_SHORTS"}}
class ReelPlayerOverlayStyle(_StrEnum):
    SHORTS: str = "REEL_PLAYER_OVERLAY_STYLE_SHORTS"


# E.g., {"reelWatchEndpoint": {"inputType": "REEL_WATCH_INPUT_TYPE_SEEDLESS"}}
class ReelWatchInputType(_StrEnum):
    SEEDLESS: str = "REEL_WATCH_INPUT_TYPE_SEEDLESS"


# E.g., {"reelWatchEndpoint": {"sequenceProvider": "REEL_WATCH_SEQUENCE_PROVIDER_RPC"}}
class ReelWatchSequenceProvider(_StrEnum):
    RPC: str = "REEL_WATCH_SEQUENCE_PROVIDER_RPC"


# A "service" as listed under "responseContext.serviceTrackingParams"
class Service(_StrEnum):
    CSI: str = "CSI"
    GFEEDBACK: str = "GFEEDBACK"
    ECATCHER: str = "ECATCHER"


class SharePanelType(Enum):
    UNIFIED_SHARE_PANEL = "SHARE_PANEL_TYPE_UNIFIED_SHARE_PANEL"


# E.g., {"signalAction": {"signal": "HELP"}}
class SignalActionSignal(_StrEnum):
    HELP: str = "HELP"


# E.g., {"signalServiceEndpoint": {"signal": "CLIENT_SIGNAL"}}
class SignalServiceSignal(_StrEnum):
    CLIENT_SIGNAL: str = "CLIENT_SIGNAL"


# E.g., {"subscribeButtonRenderer": {..., "type": "FREE"}}
class SubscribeButtonType(_StrEnum):
    FREE: str = "FREE"


class Size(_StrEnum):
    DEFAULT: str = "SIZE_DEFAULT"


class Style(_StrEnum):
    DEFAULT: str = "STYLE_DEFAULT"
    SUGGESTIVE: str = "STYLE_SUGGESTIVE"
    PRIMARY: str = "STYLE_PRIMARY"
    TEXT: str = "STYLE_TEXT"
    BLUE_TEXT: str = "STYLE_BLUE_TEXT"


# E.g., {"urlEndpoint": {"target": "TARGET_NEW_WINDOW"}}
class Target(_StrEnum):
    NEW_WINDOW: str = "TARGET_NEW_WINDOW"


# E.g., {"guideEntryRenderer": {"targetId": "library-guide-item"}}
# Note: unsure whether this should be an enum or just a str
class TargetId(_StrEnum):
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


# E.g., {"audioTracks": [{..., "visibility": "UNKNOWN"}]}
class Visibility(_StrEnum):
    UNKNOWN = "UNKNOWN"


# E.g., {"webCommandMetadata": {"webPageType": "WEB_PAGE_TYPE_BROWSE"}}
class WebPageType(_StrEnum):
    BROWSE: str = "WEB_PAGE_TYPE_BROWSE"
    CHANNEL: str = "WEB_PAGE_TYPE_CHANNEL"
    SHORTS: str = "WEB_PAGE_TYPE_SHORTS"
    UNKNOWN: str = "WEB_PAGE_TYPE_UNKNOWN"
    SETTINGS: str = "WEB_PAGE_TYPE_SETTINGS"
