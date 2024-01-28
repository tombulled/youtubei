from rich.pretty import pprint

import youtubei

# guide = youtubei.ANDROID.guide()
# guide = youtubei.IOS.guide()
# guide = youtubei.IOS_MUSIC.guide()
guide = youtubei.WEB.guide()
# guide = youtubei.WEB_REMIX.guide()

pprint(guide)
