from rich.pretty import pprint

import youtubei

"""
Notes:
    * YouTube refers to their innertube client as innerTubeTransportService?
"""

# guide = youtubei.ANDROID.guide()
# guide = youtubei.IOS.guide()
# guide = youtubei.IOS_MUSIC.guide()
guide = youtubei.WEB.guide()
# guide = youtubei.WEB_REMIX.guide()

pprint(guide)

d = youtubei.WEB.client("browse", body={"browseId": "FEwhat_to_watch"})

import json
with open("web-browse-fewhat_to_watch.json", "w") as file:
    file.write(json.dumps(d, indent=2))