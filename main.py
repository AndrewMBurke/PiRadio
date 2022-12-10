import pprint
import spotify_manager

DEVICE_ID = "be3e5f34566b9839997862f9ee997c144fb3b073"

client = spotify_manager.do_user_auth_login()
# results = client.current_user_saved_tracks()
# for idx, item in enumerate(results["items"]):
#     track = item["track"]
#     print(idx, track["artists"][0]["name"], " – ", track["name"])

# results = playlists.get_playlists(client)
# for idx, item in enumerate(results["items"]):
#     print(idx, item["name"])

# print()

# res = client.devices()
# pprint.pprint(res)

# client.start_playback(
#     device_id="6494aefb26f057bd2f44cb57d69c569be482fa3a",
#     uris=["spotify:track:6gdLoMygLsgktydTQ71b15"],
# )

client.pause_playback(device_id="be3e5f34566b9839997862f9ee997c144fb3b073")
