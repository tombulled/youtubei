from innertube import InnerTube

from youtubei import InnerTubeParser

client = InnerTube("WEB", "2.20240105.01.00")
# client = InnerTube("WEB_REMIX", "1.20220607.03.01")
# client = InnerTube("IOS", "17.14.2")
# client = InnerTube("IOS_MUSIC", "4.16.1")

parser = InnerTubeParser()

data = client.guide()

parsed = parser.parse(data)
