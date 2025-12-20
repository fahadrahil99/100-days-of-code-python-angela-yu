from http.client import HTTPException

from bs4 import BeautifulSoup
import requests
import spotipy
from requests import HTTPError
from spotipy import SpotifyException

from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID ="a67a15ecf75c454bb8a1c0bf28ccdcc0"
CLIENT_SECRET = "ed365d47c7ca4717aa5458acb5fd4804"
REDIRECT_URL = "https://example.com/callback"

sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URL,
    cache_path= "token.txt",
    scope ="playlist-modify-private playlist-modify-public",
    show_dialog=True)


sp = spotipy.Spotify(auth_manager=sp_oauth)
user_id = sp.current_user()["id"]
print(user_id)
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
Date = input("Which Year do you want to time travel to?.Type the date in this format YYYY-MM-DD : ")
# Date = "2025-12-08"
URL = f"https://www.billboard.com/charts/hot-100/{Date}/"
spotify_end_point = f"https://api.spotify.com/v1/users/{user_id}/playlists"
body = {
    "name": "Surprise Playlist",
    "description": f"Top 100 of {Date}",
    "public": False
}
year = Date.split("-")[0]

response = requests.get(url=URL,headers=header)
data = response.text
soup = BeautifulSoup(data,"html.parser")
titles = soup.select("li ul li h3")
songs = [title.getText().strip() for title in titles]
uri_list = []
for song in songs:
    try:
        track_name = songs[songs.index(song)]
        search_query = f"track:{track_name} year:{year} "
        song_uri = sp.search(q=search_query,type ="track",limit=1)
        uri_key =song_uri["tracks"]["items"][-1]["uri"].split(":",2)
        uri = uri_key[2]
        uri_list.append(uri)
    except (HTTPError,HTTPException,SpotifyException,IndexError) as e:
        print(f"The track {song} is not listed in spotify")


playlist = sp.user_playlist_create(user=user_id,name=f"{Date} Billboard 100",public=True,collaborative=False,description=f"Top 100 songs-billboard-{Date}")
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id,uri_list)








