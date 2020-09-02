import requests
from bs4 import BeautifulSoup


def reviewScrape():
    preset = "https://pitchfork.com/reviews/albums/"
    query = "rich-brian-the-sailor"

    search = preset + query + "/"

    source = requests.get(search).text

    soup = BeautifulSoup(source, 'lxml')

    review =""
    for paragraph in soup.find_all("p"):
        review = review+"\n"+paragraph.text
    print(review)


reviewScrape()
