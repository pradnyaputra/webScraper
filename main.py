from spotifyClient import *
from pitchforkClient import *

def spotifyHandler():
    artistName, albumName, albumID = getCurrentTrack()
    if artistName=="error" and albumName=="unknown":
        print("ERROR: Unknown problem while connecting to Spotify...")
        exit(1)
    if artistName=="error" and albumName=="token":
        print("ERROR: Invalid or expired Spotify access token")
        exit(1)
    if artistName=="error" and albumName=="noTrack":
        print("ERROR: No music was playing from the Spotify account")
        exit(1)

    trackList = getAlbumTracks(albumID)

    for trackDetails in trackList:
        trackDetails[2] = getTrackFeatures(trackDetails[0])


    rankedTracks=[]
    return artistName, albumName, rankedTracks

def webscrapeHandler(artist, album):
    query = convertToQuery(artist, album)
    review = reviewScrape(query)

    print(review)

def main():
    artist, album, ranked = spotifyHandler()
    webscrapeHandler(artist, album)

main()