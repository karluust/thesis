import os 
import sys
import json
import spotipy
import spotipy.util as util
import webbrowser
from json.decoder import JSONDecodeError

# Funktsioon laulude ja nende tunnuste väljastamiseks
def output_tracks():
    for i, item in enumerate(tracks['items']):

        track = item['track']
        album = sp.album(track['album']['uri'])
        
        tids = (track['uri'])
        features = sp.audio_features(tids)

        output = ["{:s}".format(track['id']),
                "{:s}".format(track['name']),
                "{:s}".format(album['name']),
                "{:s}".format(track['artists'][0]['name']),
                "{:f}".format(features[0]['acousticness']),
                "{:f}".format(features[0]['danceability']),
                "{:d}".format(track['duration_ms']),
                "{:f}".format(features[0]['energy']),
                "{:f}".format(features[0]['instrumentalness']),
                "{:d}".format(features[0]['key']),
                "{:f}".format(features[0]['liveness']),
                "{:f}".format(features[0]['loudness']),
                "{:d}".format(features[0]['mode']),
                "{:f}".format(features[0]['speechiness']),
                "{:f}".format(features[0]['tempo']),
                "{:d}".format(features[0]['time_signature']),
                "{:f}".format(features[0]['valence']),
                "{:s}".format(album['id']),
                "{:s}".format(album['release_date']),
                ]
        print(";".join(output))

# Kasutajanime ja esitusloendi ID hankimine käsurealt
username = sys.argv[1]
playlist_id = sys.argv[2]

# Vahemälu kustutamine ning kasutaja autentimine
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)


# Väljastuse päise loomine
header = ["id", "song", "album", "artist", "acousticness", "danceability", "duration_ms", "energy", "instrumentalness", 
"key", "liveness", "loudness", "mode", "speechiness", "tempo", "time_signature", "valence", "album_id", "date"]
print(";".join(header))


sp = spotipy.Spotify(auth=token)
result = sp.user_playlist(username, playlist_id, fields = "tracks,next")
tracks = result['tracks']

# Andmete väljastamine
output_tracks()
while tracks['next']:
    tracks=sp.next(tracks)
    output_tracks()