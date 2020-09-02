import requests
from bs4 import BeautifulSoup

preset ="https://pitchfork.com/reviews/albums/"
query ="rich-brian-the-sailor"

source = requests.get(preset+query).text

soup = BeautifulSoup(source, 'lxml')

result = soup.find("div", class_="contents dropcap").text

print(result)
