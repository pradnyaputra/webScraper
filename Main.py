import requests
from bs4 import BeautifulSoup


def reviewScrape():
    preset = "https://pitchfork.com/reviews/albums/"
    query = "rich-brian-the-sailor"
    search = preset + query + "/"

    source = requests.get(search).text
    soup = BeautifulSoup(source, 'lxml')
    errorFinding = soup.find("div", class_="error-page__heading")

    try:
        if(errorFinding.text)=="404":
            print("Sorry, a review can't be found on this album!")
    except:
        title = soup.title.text

        review = ""
        for paragraph in soup.find_all("p"):
            if review == "":
                review = paragraph.text
            else:
                review = review+"\n\n"+paragraph.text
        print(title)
        print(review)


reviewScrape()
