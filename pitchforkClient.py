import requests
from bs4 import BeautifulSoup

def reviewScrape(query):
    url = f"https://pitchfork.com/reviews/albums/{query}"
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    errorFinding = soup.find("div", class_="error-page__heading")

    try:
        if(errorFinding.text)=="404":
            return "Sorry, a review can't be found on this album!"
        else:
            return "There seems to be a problem displaying this page..."
    except:
        pass

    #title = soup.title.text

    review = ""
    for paragraph in soup.find_all("p"):
        if review == "":
            review = paragraph.text
        else:
            review = review+"\n\n"+paragraph.text

    return review

def convertQuery(artistName, albumName):
    query = artistName+"-"+albumName
    query = query.replace(" ","-")
    query = query.lower()
    return query.lower()