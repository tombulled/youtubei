from youtubei import WEB_REMIX
from rich.pretty import pprint as pp

# d = WEB_REMIX.browse_album("MPREb_DIJctBnvRk5") # Slaves - Are You Satisfied?
d = WEB_REMIX.client.adaptor.dispatch("browse", body={"browseId": "MPREb_DIJctBnvRk5"})

h = d["header"]["musicDetailHeaderRenderer"]
c = d["contents"]["singleColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"][
    "content"
]["sectionListRenderer"]["contents"]

p = WEB_REMIX.parser.browse_album(d)
