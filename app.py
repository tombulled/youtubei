from youtubei import InnerTubeParser
from youtubei.clients import *

# client = WEB
# client = WEB_REMIX
# client = IOS
client = IOS_MUSIC

parser = InnerTubeParser()

data = client.guide()

parsed = parser.parse(data)
