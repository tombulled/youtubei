from typing import Final

from innertube import InnerTube

__all__ = (
    "WEB",
    "WEB_REMIX",
    "IOS",
    "IOS_MUSIC",
)

WEB: Final[InnerTube] = InnerTube("WEB", "2.20240105.01.00")
WEB_REMIX: Final[InnerTube] = InnerTube("WEB_REMIX", "1.20231214.00.00")
IOS: Final[InnerTube] = InnerTube("IOS", "18.49.3")
IOS_MUSIC: Final[InnerTube] = InnerTube("IOS_MUSIC", "6.33.3")
