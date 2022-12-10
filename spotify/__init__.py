import os

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

authOptions = {
  'url': 'https://accounts.spotify.com/api/token',
  'headers': {
    'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
  },
  'form': {
    grant_type: 'client_credentials'
  },
  'json': true
}