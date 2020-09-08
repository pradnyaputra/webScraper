import requests

from pythonFiles.secrets import spotifyToken


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

def getAlbumDetails(albumID):
    endpointAlbumTracks = f"https://api.spotify.com/v1/albums/{albumID}/tracks"
    resultTracks = requests.get(endpointAlbumTracks,
                          headers={
                              "Accept": "application/json",
                              "Content-Type": "application/json",
                              "Authorization": f"Bearer {spotifyToken}"
                          }
                          )
    jsonResultTracks = resultTracks.json()


    endpointAlbumIcon = f"https://api.spotify.com/v1/albums/{albumID}"
    resultImage = requests.get(endpointAlbumIcon,
                            headers={
                                "Accept": "application/json",
                                "Content-Type": "application/json",
                                "Authorization": f"Bearer {spotifyToken}"
                            }
                            )
    jsonAlbumIcon = resultImage.json()

    coverURL = jsonAlbumIcon["images"][1]["url"]

    trackList = [[0 for i in range(3)] for j in range (len(jsonResultTracks["items"]))]

    for i in range (len(jsonResultTracks["items"])):
        trackList[i][0]=jsonResultTracks["items"][i]["id"]
        trackList[i][1]=jsonResultTracks["items"][i]["name"]
        trackList[i][2]=0

    return trackList, coverURL

def getTrackPopularity(trackID):
    endpoint = f"https://api.spotify.com/v1/tracks/{trackID}"

    result = requests.get(endpoint,
                          headers={
                              "Accept": "application/json",
                              "Content-Type": "application/json",
                              "Authorization": f"Bearer {spotifyToken}"
                          }
                          )
    jsonResult = result.json()

    popularity = jsonResult["popularity"]
    return popularity

if(__name__=="__main__"):
    pass

