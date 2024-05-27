from innertube import InnerTube
from rich.pretty import pprint as pp

from youtubei.clients import WEB_REMIX

client = InnerTube("WEB_REMIX")

d = client.adaptor.dispatch("search", body={"query": "foo fighters"})

t = d["contents"]["tabbedSearchResultsRenderer"]["tabs"][0]["tabRenderer"]
sl = t["content"]["sectionListRenderer"]
cc = sl["header"]["chipCloudRenderer"]
mcsr = sl["contents"][0]["musicCardShelfRenderer"]
msr = sl["contents"][-1]["musicShelfRenderer"]

p = WEB_REMIX.parser.search(d)
