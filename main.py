import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import keys

SPOTIFY_CLIENT_ID = keys.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = keys.SPOTIFY_CLIENT_SECRET
SPOTIFY_REDIRECT_URI = keys.SPOTIFY_REDIRECT_URI
SPOTIFY_USERNAME = keys.SPOTIFY_USERNAME

scope = None
sp = None


def get_spotify_songs():
    offset = 0
    data = []

    results = sp.current_user_saved_tracks(limit=50, offset=0)
    while results['items']:
        for idx, item in enumerate(results['items']):
            track = item['track']
            if track['available_markets']:
                data.append({'artist': track['artists'][0]['name'], 'track': track['name']})

        offset += 50
        results = sp.current_user_saved_tracks(limit=50, offset=offset)

    return data


def main():
    results = get_spotify_songs()
    with open("result.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIFY_REDIRECT_URI, scope=scope,
                                                   username=SPOTIFY_USERNAME))
    main()
