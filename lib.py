import requests as rq
import time
from random import shuffle

with open('auth_token', 'r') as f:
    auth_token = f.read().strip()

API_ENDPOINT = 'https://api.spotify.com/v1/'
HEADERS = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + auth_token
}

POPULARITY_THRESHOLD = 50

def get_playlists(q):
    q = q.replace(' ', '+')
    url = API_ENDPOINT + 'search?q=' + q + '&type=playlist'
    rep = rq.get(url, headers=HEADERS)
    data = rep.json().get('playlists', {}).get('items')
    if not data: return
    res = list()
    for d in data:
        res.append({
            'playlist_id': d.get('id'),
            'user_id': d.get('owner', {}).get('id')
        })
    return res

def get_tracks(user_id, playlist_id):
    url = API_ENDPOINT + 'users/' + str(user_id) + '/playlists/' + str(playlist_id) + '/tracks'
    rep = rq.get(url=url, headers=HEADERS)
    data = rep.json().get('items')
    if not data: return
    low_popular_tracks = low_popularity_filter(data)
    ressources = get_ressources(low_popular_tracks)
    return ressources

def low_popularity_filter(data):
    return filter(lambda d: d.get('track', {}).get('popularity') < POPULARITY_THRESHOLD, data)

def get_ressources(tracks):
    res = list()
    for t in tracks:
        track = t.get('track', {})
        res.append({
            'name': track.get('name'),
            'artists': get_artists(track),
            'previewUrl': track.get('preview_url')
        })
    return res

def get_artists(track):
    artists = track.get('artists')
    return ', '.join([a.get('name', '') for a in artists])

def process(query):
    playlists = get_playlists(query)
    res = list()
    for p in playlists:
        res += get_tracks(p.get('user_id'), p.get('playlist_id'))
        time.sleep(1)
    shuffle(res)
    return res
