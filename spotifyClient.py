import requests
from secrets import spotifyToken

def getCurrentTrack():
    endpoint = "https://api.spotify.com/v1/me/player/currently-playing"

    result = requests.get(endpoint,
                          headers={
                              "Accept": "application/json",
                              "Content-Type": "application/json",
                              "Authorization": f"Bearer {spotifyToken}"
                          }
                          )

    try:
        jsonResult = result.json()
    except:
        return "error", "noTrack", ""

    try:
        artist = jsonResult["item"]["album"]["artists"][0]["name"]
        album = jsonResult["item"]["album"]["name"]
        albumID = jsonResult["item"]["album"]["id"]
    except:
        if jsonResult["error"]["message"]=="The access token expired" or jsonResult["error"]["message"]=="Invalid access token":
            return "error", "token", ""
        else:
            return "error", "unknown", ""

    return artist, album, albumID

def getAlbumTracks(albumID):
    endpoint = f"https://api.spotify.com/v1/albums/{albumID}/tracks"

    result = requests.get(endpoint,
                          headers={
                              "Accept": "application/json",
                              "Content-Type": "application/json",
                              "Authorization": f"Bearer {spotifyToken}"
                          }
                          )
    jsonResult = result.json()

    trackList = [[0 for i in range(3)] for j in range (len(jsonResult["items"]))]

    for i in range (len(jsonResult["items"])):
        trackList[i][0]=jsonResult["items"][i]["id"]
        trackList[i][1]=jsonResult["items"][i]["name"]
        trackList[i][2]=0

    return trackList

def getTrackFeatures(trackID):
    endpoint = f"https://api.spotify.com/v1/audio-features/{trackID}"

    result = requests.get(endpoint,
                          headers={
                              "Accept": "application/json",
                              "Content-Type": "application/json",
                              "Authorization": f"Bearer {spotifyToken}"
                          }
                          )
    jsonResult = result.json()

    score = jsonResult["danceability"]+jsonResult["energy"]+jsonResult["loudness"]+jsonResult["speechiness"]+jsonResult["acousticness"]+jsonResult["instrumentalness"]+jsonResult["valence"]+jsonResult["tempo"]
    return score

if(__name__=="__main__"):
    pass
    #findCurrentTrack()

