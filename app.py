from rich.pretty import pprint as pp

from youtubei import InnerTubeParser
from youtubei.clients import *
from youtubei.parse import parse

# client = WEB
# client = WEB_REMIX
client = IOS
# client = IOS_MUSIC

parser = InnerTubeParser()

# data = client.guide()
# data = client.config()
data = client.player("ENhfIeZF_AY") # Gordon Ramsey (YT)
# data = client.player("XqoanTj5pNY") # Adele (YTM)

parsed = parser.parse(data)

pp(parsed)
