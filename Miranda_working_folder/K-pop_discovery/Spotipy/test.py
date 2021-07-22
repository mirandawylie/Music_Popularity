#Without user authentication
#import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials

#sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="65735bd07e45437880e5e856a7e463c3",
                                                           #client_secret="7c7c7ec491ae44d39038828fb985d8fc"))

#results = sp.search(q='weezer', limit=20)
#for idx, track in enumerate(results['tracks']['items']):
    #print(idx, track['name'])

#With user authentication
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="65735bd07e45437880e5e856a7e463c3",
                                               client_secret="7c7c7ec491ae44d39038828fb985d8fc",
                                               redirect_uri="http://127.0.0.1:5500",
                                               scope="user-library-read"))

results = sp.artist_top_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

