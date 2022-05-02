import telegram
import privates

token = privates.token
myId = privates.myId
all_client_id = privates.all_client_id

bot = telegram.Bot(token = token)
updates = bot.getUpdates()

for u in updates:
    print(u)


def SendAlarm(links, bAll):
    strMessage = ''
    for link in links:
        strMessage += link['title'] + ' | ' + link['url'] + '\n'

    if bAll:
        for id in all_client_id:
            bot.sendMessage(chat_id = id, text = strMessage)
    else:
        bot.sendMessage(chat_id=myId, text=strMessage)

#1. 입장 아이디를 자동적으로 수집
