from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen("https://linktr.ee/emucinema")
bsObject = BeautifulSoup(html, "html.parser")

#html에서 원하는 json부분 추출
data = {}
data = bsObject.find("script", {"id": "__NEXT_DATA__"})

#string 다듬기
start = str(data).find('>')
end = str(data).find('</script>')

processedData = str(data)[start : end]

processedData = processedData.strip('<>')

#json object로 디코딩
json_obj = json.loads(processedData)

#json에서 원하는 부분을 배열로 받기
link_array = json_obj['props']['pageProps']['account']['links']

for link in link_array:
    print(link)