from spotifyClient import *
from pitchforkClient import *

artistName, albumName = findCurrent()
query = convertQuery(artistName, albumName)
review = reviewScrape(query)

print(review)