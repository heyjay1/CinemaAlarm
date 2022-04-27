import telegram
import privates

token = privates.token
id = privates.id

bot = telegram.Bot(token = token)
updates = bot.getUpdates()

for u in updates:
    print(u)

bot.sendMessage(chat_id = id, text = 'test')