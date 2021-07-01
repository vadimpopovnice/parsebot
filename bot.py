import random
from selenium import webdriver
import config
import telebot
from telebot import types, TeleBot
import json
import requests
from time import sleep

driver = webdriver.Chrome('C:\\Program Files\\chromedriver.exe')
bot: TeleBot = telebot.TeleBot(config.token)

dictData1 = [
    {
"id": 1,
"name": "Leanne Graham",
"username": "Bret",
"email": "Sincere@april.biz",
"address": {
  "street": "Kulas Light",
  "suite": "Apt. 556",
  "city": "Gwenborough",
  "zipcode": "92998-3874",
  "geo": {
    "lat": "-37.3159",
    "lng": "81.1496"
  }
},
"phone": "1-770-736-8031 x56442",
"website": "hildegard.org",
"company": {
  "name": "Romaguera-Crona",
  "catchPhrase": "Multi-layered client-server neural-net",
  "bs": "harness real-time e-markets"
    }
}
]
dictData2 = [
    {
"id": 2,
"name": "Ervin Howell",
"username": "Antonette",
"email": "Shanna@melissa.tv",
"address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
      }
    },
"phone": "010-692-6593 x09125",
"website": "anastasia.net",
"company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
}
]
jsonData1 = json.dumps(dictData1)
dictData1 = json.loads(jsonData1)
jsonData2 = json.dumps(dictData2)
dictData2 = json.loads(jsonData2)

@bot.message_handler(commands=['latlng'])
def latlng(message):
    bot.send_message(message.chat.id,'Имя: ' + dictData2[0]['name'] + "\nЛогин: " + dictData2[0]['username'] + '\nТелефон: ' + dictData2[0]['phone'] + '\nСайт: ' + dictData2[0]['website'] + '\nКомпания: ' + dictData2[0]['company']['name'])
    bot.send_chat_action(message.from_user.id, 'find_location')
    bot.send_location(message.chat.id, latitude=dictData2[0]['address']["geo"]["lat"],
                      longitude=dictData2[0]["address"]["geo"]["lng"])


@bot.message_handler(commands=['dice'])
def dice(message):
    anum = random.randint(1, 6)
    bnum = random.randint(1, 6)
    bot.send_message(message.chat.id, f"🎲Первый кубик:",)
    bot.send_message(message.chat.id, str(anum))
    bot.send_message(message.chat.id, f"🎲Второй кубик:",)
    bot.send_message(message.chat.id, str(bnum))

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'Кинуть "кубики":\n'
                                      f'👉🏻/dice\n'
                                      f'Поиск видео YouTube:\n'
                                      f'👉🏻/search_videos\n'
                                      f'На мороженное:\n'
                                      f'👉🏻/donate\n'
                                      f'Послушать Славу Марлоу:\n'
                                      f'👉🏻/slava_marlou\n'
                                      f'Где автор?:\n'
                                      f'👉🏻/maps\n'
                                      f'Тест запроса JSON:\n'
                                      f'👉🏻/latlng\n')

@bot.message_handler(commands=['maps'])
def maps(message):
        bot.send_message(message.chat.id, 'Тут живёт автор бота!')
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, latitude=49.931578, longitude=36.429822)

@bot.message_handler(commands=['donate'])
def donate (message):
    bot.send_message(message.chat.id, f'4441114440164554')

@bot.message_handler(commands=["start"])
def start (message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.👽\n'
                                      f'Я сейчас нахожусь на стадии разработки, так что список комманд и '
                                      f'взаимодействий будет регулярно пополняться. :)\n'
                                      f'👉🏻/help\n')

@bot.message_handler(commands=['slava_marlou'])
def slava_marlou(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Пацанская версия 👊🏻", callback_data="https://www.youtube.com/watch?v=ByCfsIEmIMg"))
    keyboard.add(types.InlineKeyboardButton(text="Мужская версия 🤘🏻", callback_data="https://www.youtube.com/watch?v=vS1ZDcVWfSY"))
    bot.send_message(message.chat.id, "Ты зачем-то захотел послушать Славу Марлоу!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def button_callback(call):
    if call.message:
        if call.data == "https://www.youtube.com/watch?v=ByCfsIEmIMg":
            bot.send_message(call.message.chat.id, f'Пацанский выбор!')
            bot.send_message(call.message.chat.id, f"{call.data}")
        elif call.data == "https://www.youtube.com/watch?v=vS1ZDcVWfSY":
            bot.send_message(call.message.chat.id, f'Мужской выбор')
            bot.send_message(call.message.chat.id, f"{call.data}")


@bot.message_handler(commands=['search_videos'])
def search_videos(message):
    msg = bot.send_message(message.chat.id, 'Введите текст для поиска видео на YouTube.')
    bot.register_next_step_handler(msg, search)
def search(message):
    video_href = 'https://www.youtube.com/results?search_query=' + message.text
    driver.get(video_href)
    videos = driver.find_elements_by_id('video-title')
    # функция ниже ограничевает отправку ссылок
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 2:
            break


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f"Доброго времени суток, {message.from_user.first_name}.")
    elif message.text.lower() == 'пукич-какич':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, не тыкай пальцами в экран!")
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, f'Пока, {message.from_user.first_name}. 🤖\n'
                                          f'По вопросам работоспособности: @baguken')
    elif message.text.lower() == 'кто я?':
        bot.send_message(message.chat.id, f'К сожалению ты - {message.from_user.first_name}.')
    else:
        bot.send_message(message.chat.id, f'Извини, {message.from_user.first_name}, но я тебя не понял.\n'
                                          f'За помощью - /help')










bot.polling()