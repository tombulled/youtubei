"""
### API ###
from youtubei import WEB

data = WEB.parse_guide(...)
"""

from innertube import InnerTube
import youtubei
from rich.pretty import pprint as pp

WEB = InnerTube("WEB", "2.20240105.01.00")

guide_raw = WEB.adaptor.dispatch("guide")
data = youtubei.WEB.parse_guide(guide_raw)

pp(data)