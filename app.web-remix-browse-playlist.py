from rich.pretty import pprint as pp
from youtubei import WEB_REMIX

PLAYLIST_ID: str = "OLAK5uy_k-nVhxfuIQFO2ZE9EvqPKKM4__S3aOb_Y" # Amber Run - Philophobia
# PLAYLIST_ID: str = "OLAK5uy_khNLsz9s6ueH8YHdzORuy4PORu6tWvMrY" # Aquilo - Silhouettes
# PLAYLIST_ID: str = "RDCLAK5uy_mfdqvCAl8wodlx2P2_Ai2gNkiRDAufkkI"  # Happy Pop Hits
BROWSE_ID: str = "VL" + PLAYLIST_ID


def web_remix_browse_playlist(playlist_id: str, /):
    playlist_browse_id: str = "VL" + playlist_id

    playlist = WEB_REMIX.browse(playlist_browse_id)

    contents = playlist.contents.tabs[0].content.contents[0].contents

    songs = []

    for item in contents:
        thumbnails = item.thumbnail.thumbnail.thumbnails
        video_id = item.overlay.content.play_navigation_endpoint.command.video_id
        playlist_id = item.overlay.content.play_navigation_endpoint.command.playlist_id
        title = str(item.flex_columns[0].text)
        channel_name = str(item.flex_columns[1].text)
        channel_id = (
            item.flex_columns[1].text.runs[0].navigation_endpoint.command.browse_id
        )
        album_name = str(item.flex_columns[2].text)
        album_id = (
            item.flex_columns[2].text.runs[0].navigation_endpoint.command.browse_id
        )
        duration = str(item.fixed_columns[0].text)

        songs.append(
            dict(
                thumbnails=thumbnails,
                video_id=video_id,
                playlist_id=playlist_id,
                title=title,
                channel_name=channel_name,
                channel_id=channel_id,
                album_name=album_name,
                album_id=album_id,
                duration=duration,
            )
        )

    return songs


# d = WEB_REMIX.browse(BROWSE_ID)

# items = d.contents.tabs[0].content.contents[0].contents

# songs = []

# for item in items:
#     thumbnails = item.thumbnail.thumbnail.thumbnails
#     video_id = item.overlay.content.play_navigation_endpoint.command.video_id
#     playlist_id = item.overlay.content.play_navigation_endpoint.command.playlist_id
#     # music_video_type = (
#     #     item.overlay.content.play_navigation_endpoint.command.watch_endpoint_music_supported_configs.music_video_type
#     # )
#     title = str(item.flex_columns[0].text)
#     # video_id_2 = item.flex_columns[0].text.runs[0].navigation_endpoint.command.video_id
#     # playlist_id_2 = item.flex_columns[0].text.runs[0].navigation_endpoint.command.playlist_id
#     # music_video_type_2 = item.flex_columns[0].text.runs[0].navigation_endpoint.command.watch_endpoint_music_supported_configs.music_video_type
#     channel_name = str(item.flex_columns[1].text)
#     channel_id = item.flex_columns[1].text.runs[0].navigation_endpoint.command.browse_id
#     album_name = str(item.flex_columns[2].text)
#     album_id = item.flex_columns[2].text.runs[0].navigation_endpoint.command.browse_id
#     duration = str(item.fixed_columns[0].text)
#     # video_id_3 = item.playlist_item_data.video_id

#     songs.append(
#         dict(
#             thumbnails=item.thumbnail.thumbnail.thumbnails,
#             video_id=video_id,
#             playlist_id=playlist_id,
#             # music_video_type=music_video_type,
#             title=title,
#             # video_id_2=video_id_2,
#             # playlist_id_2=playlist_id_2,
#             # music_video_type_2=music_video_type_2,
#             channel_name=channel_name,
#             channel_id=channel_id,
#             album_name=album_name,
#             album_id=album_id,
#             duration=duration,
#             # video_id_3=video_id_3,
#         )
#     )

# d = web_remix_browse_playlist(PLAYLIST_ID)

d = WEB_REMIX.client.adaptor.dispatch("browse", body={"browseId": BROWSE_ID})
p = WEB_REMIX.parser.browse(d)
