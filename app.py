from innertube import InnerTube

from youtubei import InnerTubeParser

# client = InnerTube("WEB", "2.20240105.01.00")
# client = InnerTube("WEB_REMIX", "1.20231214.00.00")
# client = InnerTube("IOS", "18.49.3")
client = InnerTube("IOS_MUSIC", "6.33.3")

parser = InnerTubeParser()

data = client.guide()

parsed = parser.parse(data)
