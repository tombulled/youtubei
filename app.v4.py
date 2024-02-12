from rich.pretty import pprint as pp

import youtubei

"""
Notes:
    * YouTube refers to their innertube client as innerTubeTransportService?
    * Move of the business logic appears to exist in:
        desktop_polymer.js, base.js and endscreen.js
    * The following are valid request IDs (for WEB):
        GetBrowse_rid, GetGuide_rid, GetHome_rid, GetPlayer_rid,
        GetSearch_rid, GetSettings_rid, GetTrending_rid, GetWatchNext_rid,
        yt_red, yt_ad
    * Big dump of clients:
        WEB: 1,
        MWEB: 2,
        TVHTML5: 7,
        WEB_UNPLUGGED: 41,
        WEB_EMBEDDED_PLAYER: 56,
        TVHTML5_AUDIO: 57,
        TV_UNPLUGGED_CAST: 58,
        TVHTML5_KIDS: 59,
        WEB_MUSIC: 61,
        WEB_CREATOR: 62,
        TVHTML5_UNPLUGGED: 65,
        WEB_REMIX: 67,
        TVHTML5_SIMPLY: 75,
        WEB_KIDS: 76,
        TVHTML5_SIMPLY_EMBEDDED_PLAYER: 85,
        WEB_MUSIC_EMBEDDED_PLAYER: 86,
        WEB_MUSIC_ANALYTICS: 31,
        WEB_GAMING: 32,
        WEB_EXPERIMENTS: 42,
        WEB_HEROES: 60,
        WEB_UNPLUGGED_ONBOARDING: 69,
        WEB_UNPLUGGED_OPS: 70,
        WEB_UNPLUGGED_PUBLIC: 71,
        TVHTML5_VR: 72,
        TVHTML5_FOR_KIDS: 93
    * List known renderers/models using: grep -Po "(?<=g.Lw\(').+(?=')" resources/base.js
        Suffixes: Renderer, Endpoint, Model, Group, Command, Metadata, Action, Directives, Response, Vars
        Note: This is not exhaustive (e.g. no guide items?)
    * desktop_polymer.js looks more valuable than base.js
    * List (all?) known renderers/models using: grep -Po "(?<=new fl\(').+(?='\);)"  resources/desktop_polymer.js
    * "Actions" are potentially Redux actions
    * Commands can contain endpoints and actions
    * Endpoints can contain actions
    * serviceEndpoint's are commands that contain an endpoint!
"""

# guide = youtubei.ANDROID.guide()
# guide = youtubei.IOS.guide()
# guide = youtubei.IOS_MUSIC.guide()
# guide = youtubei.WEB.guide()
# guide = youtubei.WEB_REMIX.guide()
c = youtubei.WEB
# c = youtubei.WEB_REMIX

d = c.client.adaptor.dispatch("guide")

pp(d)

p = c.parser.guide(d)

pp(p)

# d = youtubei.WEB.client("browse", body={"browseId": "FEwhat_to_watch"})

# import json
# with open("web-browse-fewhat_to_watch.json", "w") as file:
#     file.write(json.dumps(d, indent=2))
