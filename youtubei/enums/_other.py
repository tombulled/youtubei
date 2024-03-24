from enum import Enum

# __all__ = (
#     "ActiveViewTrafficType",
#     "AdPlacementKind",
#     "BackgroundPromoStyleType",
#     "CaptionsInitialState",
#     "HeaderType",
#     "MusicPageType",
#     "LanguageCode",
#     "PlaybackMode",
#     "ReelPlayerNavigationModel",
#     "ReelPlayerOverlayStyle",
#     "ReelWatchInputType",
#     "ReelWatchSequenceProvider",
#     "Service",
#     "SharePanelType",
#     "Signal",
#     "Size",
#     "Style",
#     "Target",
#     "TargetId",
#     "WebPageType",
# )


class _StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class ActiveViewTrafficType(_StrEnum):
    VIDEO = "ACTIVE_VIEW_TRAFFIC_TYPE_VIDEO"


# E.g., {"adPlacementConfig": {"kind": "AD_PLACEMENT_KIND_START"}}
class AdPlacementKind(_StrEnum):
    END = "AD_PLACEMENT_KIND_END"
    MILLISECONDS = "AD_PLACEMENT_KIND_MILLISECONDS"
    START = "AD_PLACEMENT_KIND_START"


# E.g., {"backgroundPromoRenderer": {"style": {"value": "BACKGROUND_PROMO_STYLE_TYPE_EMPTY_STATE"}}}
class BackgroundPromoStyleType(_StrEnum):
    EMPTY_STATE = "BACKGROUND_PROMO_STYLE_TYPE_EMPTY_STATE"


class BadgeStyleType(_StrEnum):
    PREMIUM: str = "BADGE_STYLE_TYPE_PREMIUM"
    SIMPLE: str = "BADGE_STYLE_TYPE_SIMPLE"
    AD: str = "BADGE_STYLE_TYPE_AD"
    LIVE_NOW: str = "BADGE_STYLE_TYPE_LIVE_NOW"
    UNIFIED_VERIFIED: str = "BADGE_STYLE_TYPE_UNIFIED_VERIFIED"
    SHORTS_PLAYER: str = "BADGE_STYLE_TYPE_SHORTS_PLAYER"


class CaptionsInitialState(_StrEnum):
    OFF_RECOMMENDED = "CAPTIONS_INITIAL_STATE_OFF_RECOMMENDED"


# E.g., {"playerMicroformatRenderer": {"category": "Entertainment"}}
class Category(_StrEnum):
    ENTERTAINMENT: str = "Entertainment"
    MUSIC: str = "Music"


class CheckboxCheckedState(_StrEnum):
    UNCHECKED: str = "CHECKBOX_CHECKED_STATE_UNCHECKED"


# E.g., {"playerMicroformatRenderer": {"availableCountries": ["AD", "AE", ...]}}
class CountryCode(_StrEnum):
    AD: str = "AD"
    AE: str = "AE"
    AF: str = "AF"
    AG: str = "AG"
    AI: str = "AI"
    AL: str = "AL"
    AM: str = "AM"
    AO: str = "AO"
    AQ: str = "AQ"
    AR: str = "AR"
    AS: str = "AS"
    AT: str = "AT"
    AU: str = "AU"
    AW: str = "AW"
    AX: str = "AX"
    AZ: str = "AZ"
    BA: str = "BA"
    BB: str = "BB"
    BD: str = "BD"
    BE: str = "BE"
    BF: str = "BF"
    BG: str = "BG"
    BH: str = "BH"
    BI: str = "BI"
    BJ: str = "BJ"
    BL: str = "BL"
    BM: str = "BM"
    BN: str = "BN"
    BO: str = "BO"
    BQ: str = "BQ"
    BR: str = "BR"
    BS: str = "BS"
    BT: str = "BT"
    BV: str = "BV"
    BW: str = "BW"
    BY: str = "BY"
    BZ: str = "BZ"
    CA: str = "CA"
    CC: str = "CC"
    CD: str = "CD"
    CF: str = "CF"
    CG: str = "CG"
    CH: str = "CH"
    CI: str = "CI"
    CK: str = "CK"
    CL: str = "CL"
    CM: str = "CM"
    CN: str = "CN"
    CO: str = "CO"
    CR: str = "CR"
    CU: str = "CU"
    CV: str = "CV"
    CW: str = "CW"
    CX: str = "CX"
    CY: str = "CY"
    CZ: str = "CZ"
    DE: str = "DE"
    DJ: str = "DJ"
    DK: str = "DK"
    DM: str = "DM"
    DO: str = "DO"
    DZ: str = "DZ"
    EC: str = "EC"
    EE: str = "EE"
    EG: str = "EG"
    EH: str = "EH"
    ER: str = "ER"
    ES: str = "ES"
    ET: str = "ET"
    FI: str = "FI"
    FJ: str = "FJ"
    FK: str = "FK"
    FM: str = "FM"
    FO: str = "FO"
    FR: str = "FR"
    GA: str = "GA"
    GB: str = "GB"
    GD: str = "GD"
    GE: str = "GE"
    GF: str = "GF"
    GG: str = "GG"
    GH: str = "GH"
    GI: str = "GI"
    GL: str = "GL"
    GM: str = "GM"
    GN: str = "GN"
    GP: str = "GP"
    GQ: str = "GQ"
    GR: str = "GR"
    GS: str = "GS"
    GT: str = "GT"
    GU: str = "GU"
    GW: str = "GW"
    GY: str = "GY"
    HK: str = "HK"
    HM: str = "HM"
    HN: str = "HN"
    HR: str = "HR"
    HT: str = "HT"
    HU: str = "HU"
    ID: str = "ID"
    IE: str = "IE"
    IL: str = "IL"
    IM: str = "IM"
    IN: str = "IN"
    IO: str = "IO"
    IQ: str = "IQ"
    IR: str = "IR"
    IS: str = "IS"
    IT: str = "IT"
    JE: str = "JE"
    JM: str = "JM"
    JO: str = "JO"
    JP: str = "JP"
    KE: str = "KE"
    KG: str = "KG"
    KH: str = "KH"
    KI: str = "KI"
    KM: str = "KM"
    KN: str = "KN"
    KP: str = "KP"
    KR: str = "KR"
    KW: str = "KW"
    KY: str = "KY"
    KZ: str = "KZ"
    LA: str = "LA"
    LB: str = "LB"
    LC: str = "LC"
    LI: str = "LI"
    LK: str = "LK"
    LR: str = "LR"
    LS: str = "LS"
    LT: str = "LT"
    LU: str = "LU"
    LV: str = "LV"
    LY: str = "LY"
    MA: str = "MA"
    MC: str = "MC"
    MD: str = "MD"
    ME: str = "ME"
    MF: str = "MF"
    MG: str = "MG"
    MH: str = "MH"
    MK: str = "MK"
    ML: str = "ML"
    MM: str = "MM"
    MN: str = "MN"
    MO: str = "MO"
    MP: str = "MP"
    MQ: str = "MQ"
    MR: str = "MR"
    MS: str = "MS"
    MT: str = "MT"
    MU: str = "MU"
    MV: str = "MV"
    MW: str = "MW"
    MX: str = "MX"
    MY: str = "MY"
    MZ: str = "MZ"
    NA: str = "NA"
    NC: str = "NC"
    NE: str = "NE"
    NF: str = "NF"
    NG: str = "NG"
    NI: str = "NI"
    NL: str = "NL"
    NO: str = "NO"
    NP: str = "NP"
    NR: str = "NR"
    NU: str = "NU"
    NZ: str = "NZ"
    OM: str = "OM"
    PA: str = "PA"
    PE: str = "PE"
    PF: str = "PF"
    PG: str = "PG"
    PH: str = "PH"
    PK: str = "PK"
    PL: str = "PL"
    PM: str = "PM"
    PN: str = "PN"
    PR: str = "PR"
    PS: str = "PS"
    PT: str = "PT"
    PW: str = "PW"
    PY: str = "PY"
    QA: str = "QA"
    RE: str = "RE"
    RO: str = "RO"
    RS: str = "RS"
    RU: str = "RU"
    RW: str = "RW"
    SA: str = "SA"
    SB: str = "SB"
    SC: str = "SC"
    SD: str = "SD"
    SE: str = "SE"
    SG: str = "SG"
    SH: str = "SH"
    SI: str = "SI"
    SJ: str = "SJ"
    SK: str = "SK"
    SL: str = "SL"
    SM: str = "SM"
    SN: str = "SN"
    SO: str = "SO"
    SR: str = "SR"
    SS: str = "SS"
    ST: str = "ST"
    SV: str = "SV"
    SX: str = "SX"
    SY: str = "SY"
    SZ: str = "SZ"
    TC: str = "TC"
    TD: str = "TD"
    TF: str = "TF"
    TG: str = "TG"
    TH: str = "TH"
    TJ: str = "TJ"
    TK: str = "TK"
    TL: str = "TL"
    TM: str = "TM"
    TN: str = "TN"
    TO: str = "TO"
    TR: str = "TR"
    TT: str = "TT"
    TV: str = "TV"
    TW: str = "TW"
    TZ: str = "TZ"
    UA: str = "UA"
    UG: str = "UG"
    UM: str = "UM"
    US: str = "US"
    UY: str = "UY"
    UZ: str = "UZ"
    VA: str = "VA"
    VC: str = "VC"
    VE: str = "VE"
    VG: str = "VG"
    VI: str = "VI"
    VN: str = "VN"
    VU: str = "VU"
    WF: str = "WF"
    WS: str = "WS"
    YE: str = "YE"
    YT: str = "YT"
    ZA: str = "ZA"
    ZM: str = "ZM"
    ZW: str = "ZW"


class EndscreenElementStyle(_StrEnum):
    VIDEO = "VIDEO"
    PLAYLIST = "PLAYLIST"


# E.g., {"changeEngagementPanelVisibilityAction": {"visibility": "ENGAGEMENT_PANEL_VISIBILITY_EXPANDED"}}
class EngagementPanelVisibility(_StrEnum):
    EXPANDED: str = "ENGAGEMENT_PANEL_VISIBILITY_EXPANDED"


# E.g., {"audioOnlyPlayabilityRenderer": {"audioOnlyAvailability": "FEATURE_AVAILABILITY_ALLOWED"}}
class FeatureAvailability(_StrEnum):
    ALLOWED = "FEATURE_AVAILABILITY_ALLOWED"


class HeaderType(_StrEnum):
    USER_AUTH: str = "USER_AUTH"
    VISITOR_ID: str = "VISITOR_ID"
    PLUS_PAGE_ID: str = "PLUS_PAGE_ID"


# E.g., {"icon": {"iconType": "TAB_HOME"}}
# class IconType(_StrEnum):
#     # WEB_REMIX
#     LIBRARY_MUSIC = "LIBRARY_MUSIC"
#     TAB_EXPLORE = "TAB_EXPLORE"
#     TAB_HOME = "TAB_HOME"
#     ERROR_OUTLINE = "ERROR_OUTLINE"
#     OPEN_IN_NEW = "OPEN_IN_NEW"
#     INFO_OUTLINE = "INFO_OUTLINE"
#     # WEB
#     WHAT_TO_WATCH = "WHAT_TO_WATCH"
#     TAB_SHORTS = "TAB_SHORTS"
#     SUBSCRIPTIONS = "SUBSCRIPTIONS"
#     HELP = "HELP"
#     SETTINGS = "SETTINGS"
#     VIDEO_LIBRARY_WHITE = "VIDEO_LIBRARY_WHITE"
#     WATCH_HISTORY = "WATCH_HISTORY"
#     YOUTUBE_ROUND = "YOUTUBE_ROUND"
#     AVATAR_LOGGED_OUT = "AVATAR_LOGGED_OUT"
#     TRENDING = "TRENDING"
#     SHOPPING_BAG = "SHOPPING_BAG"
#     MUSIC = "MUSIC"
#     CLAPPERBOARD = "CLAPPERBOARD"
#     LIVE = "LIVE"
#     GAMING_LOGO = "GAMING_LOGO"
#     NEWS = "NEWS"
#     TROPHY = "TROPHY"
#     COURSE = "COURSE"
#     FASHION_LOGO = "FASHION_LOGO"
#     BROADCAST = "BROADCAST"
#     ADD_CIRCLE = "ADD_CIRCLE"
#     UNPLUGGED_LOGO = "UNPLUGGED_LOGO"
#     YOUTUBE_MUSIC = "YOUTUBE_MUSIC"
#     YOUTUBE_KIDS_ROUND = "YOUTUBE_KIDS_ROUND"
#     FLAG = "FLAG"
#     FEEDBACK = "FEEDBACK"
#     INFO = "INFO"
#     # IOS
#     TAB_SUBSCRIPTIONS = "TAB_SUBSCRIPTIONS"
#     TAB_ACTIVITY = "TAB_ACTIVITY"
#     SEARCH = "SEARCH"
#     ACCOUNT_CIRCLE = "ACCOUNT_CIRCLE"
#     UNPLUGGED_RED_LOGO = "UNPLUGGED_RED_LOGO"
#     MUSIC_RED_LOGO = "MUSIC_RED_LOGO"
#     KIDS_RED_LOGO = "KIDS_RED_LOGO"
#     YOUTUBE_LOGO = "YOUTUBE_LOGO"
#     # IOS_MUSIC
#     TAB_SAMPLES = "TAB_SAMPLES"
#     # ANDROID
#     PIVOT_HOME = "PIVOT_HOME"
#     PIVOT_SUBSCRIPTIONS = "PIVOT_SUBSCRIPTIONS"


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


# E.g., {"adLayoutMetadata": {"layoutType": "LAYOUT_TYPE_COMPOSITE_PLAYER_BYTES"}}
class LayoutType(_StrEnum):
    COMPOSITE_PLAYER_BYTES = "LAYOUT_TYPE_COMPOSITE_PLAYER_BYTES"
    MEDIA = "LAYOUT_TYPE_MEDIA"

class LikeStatus(_StrEnum):
    INDIFFERENT: str = "INDIFFERENT"

class MultiPageMenuStyleType(_StrEnum):
    SYSTEM = "MULTI_PAGE_MENU_STYLE_TYPE_SYSTEM"
    REPORT_CHANNEL = "MULTI_PAGE_MENU_STYLE_TYPE_REPORT_CHANNEL"


# E.g., {"browseEndpointContextMusicConfig": {"pageType": "MUSIC_PAGE_TYPE_METRONOME"}}
class MusicPageType(_StrEnum):
    METRONOME = "MUSIC_PAGE_TYPE_METRONOME"
    ALBUM = "MUSIC_PAGE_TYPE_ALBUM"
    ARTIST = "MUSIC_PAGE_TYPE_ARTIST"


# E.g. {'miniplayerRenderer': {'playbackMode': 'PLAYBACK_MODE_ALLOW'}}
class PlaybackMode(_StrEnum):
    ALLOW = "PLAYBACK_MODE_ALLOW"


class PlaylistEditListType(_StrEnum):
    QUEUE = "PLAYLIST_EDIT_LIST_TYPE_QUEUE"


# E.g., {"openPopupAction": {"type": "DIALOG"}}
class PopupType(_StrEnum):
    DIALOG = "DIALOG"
    DROPDOWN = "DROPDOWN"


class Privacy(_StrEnum):
    UNLISTED: str = "UNLISTED"


class QueueInsertPosition(_StrEnum):
    INSERT_AFTER_CURRENT_VIDEO: str = "INSERT_AFTER_CURRENT_VIDEO"
    INSERT_AT_END: str = "INSERT_AT_END"


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
    GUIDED_HELP: str = "GUIDED_HELP"
    ECATCHER: str = "ECATCHER"
    BREAKPAD: str = "BREAKPAD"
    GOOGLE_HELP: str = "GOOGLE_HELP"
    LISTNR: str = "LISTNR"


class SharePanelType(Enum):
    UNIFIED_SHARE_PANEL = "SHARE_PANEL_TYPE_UNIFIED_SHARE_PANEL"


# E.g., {"signalAction": {"signal": "HELP"}}
class Signal(_StrEnum):
    HELP: str = "HELP"
    CLIENT_SIGNAL: str = "CLIENT_SIGNAL"
    HISTORY_BACK: str = "HISTORY_BACK"
    HISTORY_FORWARD: str = "HISTORY_FORWARD"
    SKIP_NAVIGATION: str = "SKIP_NAVIGATION"
    LOAD_GUIDE: str = "LOAD_GUIDE"
    DELETE_PLAYLIST_DOWNLOAD: str = "DELETE_PLAYLIST_DOWNLOAD"
    DELETE_DOWNLOAD: str = "DELETE_DOWNLOAD"
    UNDO_DELETE_DOWNLOAD: str = "UNDO_DELETE_DOWNLOAD"
    SOFT_RELOAD_PAGE: str = "SOFT_RELOAD_PAGE"
    SCROLL_TO_COMMENTS: str = "SCROLL_TO_COMMENTS"
    DELETE_ALL_DOWNLOADS: str = "DELETE_ALL_DOWNLOADS"
    GET_DATASYNC_IDS: str = "GET_DATASYNC_IDS"
    GET_ACCOUNT_MENU: str = "GET_ACCOUNT_MENU"


# E.g., {"adSlotMetadata": {"triggerEvent": "SLOT_TRIGGER_EVENT_BEFORE_CONTENT"}}
class SlotTriggerEvent(_StrEnum):
    BEFORE_CONTENT = "SLOT_TRIGGER_EVENT_BEFORE_CONTENT"


# E.g., {"adSlotMetadata": {"slotType": "SLOT_TYPE_PLAYER_BYTES"}}
class SlotType(_StrEnum):
    PLAYER_BYTES = "SLOT_TYPE_PLAYER_BYTES"


# E.g., {"subscribeButtonRenderer": {..., "type": "FREE"}}
class SubscribeButtonType(_StrEnum):
    FREE: str = "FREE"


class Size(_StrEnum):
    DEFAULT: str = "SIZE_DEFAULT"
    SMALL: str = "SIZE_SMALL"


class Style(_StrEnum):
    BLUE_TEXT: str = "STYLE_BLUE_TEXT"
    DEFAULT: str = "STYLE_DEFAULT"
    PRIMARY: str = "STYLE_PRIMARY"
    SUGGESTIVE: str = "STYLE_SUGGESTIVE"
    TEXT: str = "STYLE_TEXT"
    UNKNOWN: str = "STYLE_UNKNOWN"
    MONO_FILLED: str = "STYLE_MONO_FILLED"
    MONO_TONAL: str = "STYLE_MONO_TONAL"
    BRAND: str = "STYLE_BRAND"
    MONO_TONAL_OVERLAY: str = "STYLE_MONO_TONAL_OVERLAY"
    MONO_FILLED_OVERLAY: str = "STYLE_MONO_FILLED_OVERLAY"
    DARK_ON_WHITE: str = "STYLE_DARK_ON_WHITE"


# E.g., {"urlEndpoint": {"target": "TARGET_NEW_WINDOW"}}
class Target(_StrEnum):
    NEW_WINDOW: str = "TARGET_NEW_WINDOW"


# E.g., {"guideEntryRenderer": {"targetId": "library-guide-item"}}
# Note: unsure whether this should be an enum or just a str
class TargetId(_StrEnum):
    # YouTube Web
    LIBRARY_GUIDE_ITEM = "library-guide-item"
    ENGAGEMENT_PANEL_ERROR_CORRECTIONS = "engagement-panel-error-corrections"
    TOPBAR_SIGNIN = "topbar-signin"
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


# E.g., {"thumbnailOverlayTimeStatusRenderer": {"style": "DEFAULT"}}
class ThumbnailOverlayTimeStatusStyle(_StrEnum):
    DEFAULT = "DEFAULT"


# E.g., {"audioTracks": [{..., "visibility": "UNKNOWN"}]}
class Visibility(_StrEnum):
    UNKNOWN = "UNKNOWN"


# E.g., {"webCommandMetadata": {"webPageType": "WEB_PAGE_TYPE_BROWSE"}}
class WebPageType(_StrEnum):
    BROWSE: str = "WEB_PAGE_TYPE_BROWSE"
    CHANNEL: str = "WEB_PAGE_TYPE_CHANNEL"
    SETTINGS: str = "WEB_PAGE_TYPE_SETTINGS"
    SHORTS: str = "WEB_PAGE_TYPE_SHORTS"
    UNKNOWN: str = "WEB_PAGE_TYPE_UNKNOWN"
    WATCH: str = "WEB_PAGE_TYPE_WATCH"
    PLAYLIST: str = "WEB_PAGE_TYPE_PLAYLIST"
    SEARCH: str = "WEB_PAGE_TYPE_SEARCH"
    OPEN_IN_APP: str = "WEB_PAGE_TYPE_OPEN_IN_APP"
    MINI_APP: str = "WEB_PAGE_TYPE_MINI_APP"


class WatchBreakType(_StrEnum):
    DATA_REMINDER = "WATCH_BREAK_TYPE_DATA_REMINDER"
