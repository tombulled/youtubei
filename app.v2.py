"""
### API ###
from youtubei import WEB

data = WEB.parse_guide(...)
"""

from innertube import InnerTube
from rich.pretty import pprint as pp

import youtubei

WEB = InnerTube("WEB", "2.20240105.01.00")


class WEB:
    client = InnerTube("WEB", "2.20240105.01.00")
    parser = youtubei.WEB

    @classmethod
    def guide(cls):
        response = cls.client.adaptor.dispatch("guide")

        return cls.parser.parse_guide(response)


# guide_raw = WEB.adaptor.dispatch("guide")
# data = youtubei.WEB.parse_guide(guide_raw)

d = WEB.guide()

pp(d)
