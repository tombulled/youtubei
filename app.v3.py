from innertube import InnerTube
from rich.pretty import pprint as pp

import youtubei

"""
Notes:
    * Services share renderers, e.g. YouTube and YouTube Music
        both use GuideSectionRenderer
"""

# client, parser = InnerTube("WEB", "2.20240105.01.00"), youtubei.WEB
client, parser = InnerTube("WEB_REMIX", "1.20231214.00.00"), youtubei.WEB_REMIX
# client, parser = InnerTube("IOS", "18.49.3"), youtubei.IOS
# client, parser = InnerTube("IOS_MUSIC", "6.33.3"), youtubei.IOS_MUSIC
# client, parser = InnerTube("ANDROID", "19.03.35"), youtubei.ANDROID

d = client.adaptor.dispatch("guide")
p = parser.guide(d)

pp(p)
