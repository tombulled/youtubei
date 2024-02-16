from rich.pretty import pprint as pp

from youtubei import WEB

# Amber Run - Philophobia
PLAYLIST_ID: str = "OLAK5uy_k-nVhxfuIQFO2ZE9EvqPKKM4__S3aOb_Y"

d = WEB.client.adaptor.dispatch("browse", body={"browseId": "VL" + PLAYLIST_ID})

pp(d)

p = WEB.parser.browse(d)

pp(p)
