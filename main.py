from spotifyClient import *
from pitchforkClient import *

artistName, albumName = findCurrent()
if artistName=="error" and albumName=="error":
    print("ERROR: Having trouble reaching Spotify...")
    exit(1)
if artistName=="error" and albumName=="token":
    print("ERROR: Invalid Spotify access token")
    exit(1)

query = convertQuery(artistName, albumName)
review = reviewScrape(query)

print(review)