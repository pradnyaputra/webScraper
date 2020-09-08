from pythonFiles.pitchforkClient import reviewScrape
from pythonFiles.spotifyClient import *
from pythonFiles.interface import *


def spotifyHandler():
    artistName, albumName, albumID = getCurrentTrack()
    if artistName=="error" and albumName=="unknown":
        return "ERROR","Unknown problem while connecting to Spotify...",0,0
    if artistName=="error" and albumName=="token":
        return "ERROR","Invalid or expired Spotify access token",0,0
    if artistName=="error" and albumName=="noTrack":
        return "ERROR","No music playing from the Spotify account",0,0

    trackList, coverURL = getAlbumDetails(albumID)

    for trackDetails in trackList:
        trackDetails[2] = getTrackPopularity(trackDetails[0])
    rankedTracks=rankAlbumTracks(trackList)

    return artistName, albumName, coverURL, rankedTracks

def webscrapeHandler(artist, album):
    query = convertToQuery(artist, album)
    review = reviewScrape(query)

    return review

def convertToQuery(artistName, albumName):
    query = artistName+"-"+albumName

    query = query.replace(" (Deluxe)", "")
    query = query.replace(" - ", "-")
    query = query.replace("_", "")
    query = query.replace("/","")
    query = query.replace("\\","")
    query = query.replace(")", "")
    query = query.replace("(", "")
    query = query.replace("'", "")
    query = query.replace('"', "")
    query = query.replace(",", "")
    query = query.replace(".", "")
    query = query.replace(" ","-")
    query = query.replace("&", "and")

    return query.lower()

def rankAlbumTracks(trackList):

    #sorting the 2D list via insertion sort due to efficiency
    for i in range(1, len(trackList)):

        key0 = trackList[i][0]
        key1 = trackList[i][1]
        key2 = trackList[i][2]


        j = i - 1
        while j >= 0 and key2 > trackList[j][2]:
            trackList[j + 1][0] = trackList[j][0]
            trackList[j + 1][1] = trackList[j][1]
            trackList[j + 1][2] = trackList[j][2]

            j -= 1
            trackList[j + 1][0] = key0
            trackList[j + 1][1] = key1
            trackList[j + 1][2] = key2

    return trackList

