from rich.pretty import pprint as pp

from youtubei import InnerTubeParser
from youtubei.clients import *
from youtubei.parsers import parse_guide

"""
import youtubei

d = youtube.parse(...)
"""

client = WEB
# client = WEB_REMIX
# client = IOS
# client = IOS_MUSIC

parser = InnerTubeParser()

data = client.adaptor.dispatch("guide")
# data = client.config()
# data = client.player("ENhfIeZF_AY") # Gordon Ramsey (YT)
# data = client.player("XqoanTj5pNY") # Adele (YTM)

# parsed = parser.parse(data)
parsed = parse_guide(data)

d = data
p = parsed

pp(parsed)
