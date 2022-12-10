import spotipy
from spotipy.oauth2 import SpotifyOAuth

from typing import Optional

REDIRECT_URI = "http://localhost:5000/callback"
# os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_ID = "0eab9ed2035f4023984c58fa6e3baef7"
# os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_CLIENT_SECRET = "1004cea11fde47e6a1c6e5bb7bdd732f"

SCOPES = [
    "user-library-read",
    "user-read-private",
    "user-read-email",
    "playlist-read-private",
    "playlist-read-collaborative",
    "user-read-playback-state",
    "user-modify-playback-state",
]


def do_user_auth_login() -> spotipy.Spotify:
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=" ".join(SCOPES),
        )
    )


def get_playlists(client: spotipy.Spotify) -> dict:
    """Get the playlists for the current user.

    Args:
        client (spotipy.Spotify): The client to use.
    """
    json_returned = client.current_user_playlists()
    return json_returned["items"]


def play(
    client: spotipy.Spotify,
    device_id: str,
    context_uri: Optional[str] = None,
    track_uri: Optional[str] = None,
):
    """Start or resume playback.

    Args:
        client (spotipy.Spotify): The client to use.
        device_id (str): The device to play on.
        context_uri (str, optional): The context uri to play. Defaults to None.
        track_uri (str, optional): The track uri to play. Defaults to None.
    """
    if context_uri:
        client.start_playback(device_id=device_id, context_uri=context_uri)
    else:
        client.start_playback(device_id=device_id, uris=[track_uri])


def pause(client: spotipy.Spotify, device_id: str):
    """Pause playback.

    Args:
        client (spotipy.Spotify): The client to use.
        device_id (str): The device to pause.
    """
    client.pause_playback(device_id=device_id)
