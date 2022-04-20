from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen("https://linktr.ee/emucinema")
bsObject = BeautifulSoup(html, "html.parser")

data = {}
data = bsObject.find("script", {"id": "__NEXT_DATA__"})
print(data)

# print(bsObject.div)