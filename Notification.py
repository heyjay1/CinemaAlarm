from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import privates
import TelegramBot
import schedule

def ScrapHTML():
    html = urlopen("https://linktr.ee/emucinema")
    bsObject = BeautifulSoup(html, "html.parser")

    #html에서 원하는 json부분 추출
    data = {}
    data = bsObject.find("script", {"id": "__NEXT_DATA__"})

    return data

def MakeJSONData(data):
    #string 다듬기
    start = str(data).find('>')
    end = str(data).find('</script>')

    processedData = str(data)[start : end]

    processedData = processedData.strip('<>')

    #json object로 디코딩
    json_obj = json.loads(processedData)

    return json_obj

def scrap():
    data = ScrapHTML()
    json_obj = MakeJSONData(data)

    #json에서 원하는 부분을 배열로 받기
    link_array = json_obj['props']['pageProps']['account']['links']

    new_title = []
    new_id = []
    for link in link_array:
        new_title.append(link['title'])
        new_id.append(link['id'])
    print(new_title, new_id)

    if (new_title != privates.link_title) or (new_id != privates.link_id):
        TelegramBot.SendAlarm(link_array, True)
    else:
        TelegramBot.SendAlarm(link_array, False)

def main():
    schedule.every(1).minutes.do(scrap)
    while True:
        schedule.run_pending()        

if __name__ == '__main__':
    main()

#3. 1분단위로 스크롤링?