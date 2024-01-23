from innertube import InnerTube
import youtubei
from rich.pretty import pprint as pp

"""
Notes:
    * Services share renderers, e.g. YouTube and YouTube Music
        both use GuideSectionRenderer
"""

WEB_REMIX = InnerTube("WEB_REMIX", "1.20231214.00.00")

d = WEB_REMIX.adaptor.dispatch("guide")
p = youtubei.WEB_REMIX.parse_guide(d)

pp(p)
