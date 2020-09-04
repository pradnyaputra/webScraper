import requests
from secrets import spotifyToken

def findCurrent():
    endpoint = "https://api.spotify.com/v1/me/player/currently-playing"

    result = requests.get(endpoint,
                          headers={
                              "Accept": "application/json",
                              "Content-Type": "application/json",
                              "Authorization": f"Bearer {spotifyToken}"
                          }
                          )

    jsonFormat = result.json()

    artist = jsonFormat["item"]["album"]["artists"][0]["name"]
    album = jsonFormat["item"]["album"]["name"]

    return artist, album

if(__name__=="__main__"):
    findCurrent()