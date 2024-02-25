from rich.pretty import pprint as pp
from youtubei import WEB_REMIX

# Aquilo - Silhouettes
PLAYLIST_ID: str = "OLAK5uy_khNLsz9s6ueH8YHdzORuy4PORu6tWvMrY"
BROWSE_ID: str = "VL" + PLAYLIST_ID

# d = WEB_REMIX.browse("VL" + PLAYLIST_ID)
d = WEB_REMIX.client.adaptor.dispatch("browse", body={"browseId": BROWSE_ID})

# Note: here last. youtube may provide 1200x1200 artwork,
#   however the overall quality of the data is worse. web remix it is.
# No! WEB is important as it has the "audio" videos instead of the music videos.
# Maybe need to use a combination?

p = WEB_REMIX.parser.browse(d)
