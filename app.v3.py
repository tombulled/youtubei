from innertube import InnerTube
import youtubei
from rich.pretty import pprint as pp

"""
Notes:
    * Services share renderers, e.g. YouTube and YouTube Music
        both use GuideSectionRenderer
"""

client, parser = InnerTube("WEB", "2.20240105.01.00"), youtubei.WEB
# client, parser = InnerTube("WEB_REMIX", "1.20231214.00.00"), youtubei.WEB_REMIX
# IOS = InnerTube("IOS", "18.49.3")
# IOS_MUSIC = InnerTube("IOS_MUSIC", "6.33.3")

d = client.adaptor.dispatch("guide")
p = parser.parse_guide(d)

pp(p)
