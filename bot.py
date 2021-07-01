import random
from selenium import webdriver
import config
import telebot
from telebot import types, TeleBot
import json
import requests
from time import sleep
import time

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
  },
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
  },
  {
    "id": 3,
    "name": "Clementine Bauch",
    "username": "Samantha",
    "email": "Nathan@yesenia.net",
    "address": {
      "street": "Douglas Extension",
      "suite": "Suite 847",
      "city": "McKenziehaven",
      "zipcode": "59590-4157",
      "geo": {
        "lat": "-68.6102",
        "lng": "-47.0653"
      }
    },
    "phone": "1-463-123-4447",
    "website": "ramiro.info",
    "company": {
      "name": "Romaguera-Jacobson",
      "catchPhrase": "Face to face bifurcated interface",
      "bs": "e-enable strategic applications"
    }
  },
  {
    "id": 4,
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner@kory.org",
    "address": {
      "street": "Hoeger Mall",
      "suite": "Apt. 692",
      "city": "South Elvis",
      "zipcode": "53919-4257",
      "geo": {
        "lat": "29.4572",
        "lng": "-164.2990"
      }
    },
    "phone": "493-170-9623 x156",
    "website": "kale.biz",
    "company": {
      "name": "Robel-Corkery",
      "catchPhrase": "Multi-tiered zero tolerance productivity",
      "bs": "transition cutting-edge web services"
    }
  },
  {
    "id": 5,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
    "address": {
      "street": "Skiles Walks",
      "suite": "Suite 351",
      "city": "Roscoeview",
      "zipcode": "33263",
      "geo": {
        "lat": "-31.8129",
        "lng": "62.5342"
      }
    },
    "phone": "(254)954-1289",
    "website": "demarco.info",
    "company": {
      "name": "Keebler LLC",
      "catchPhrase": "User-centric fault-tolerant solution",
      "bs": "revolutionize end-to-end systems"
    }
  },
  {
    "id": 6,
    "name": "Mrs. Dennis Schulist",
    "username": "Leopoldo_Corkery",
    "email": "Karley_Dach@jasper.info",
    "address": {
      "street": "Norberto Crossing",
      "suite": "Apt. 950",
      "city": "South Christy",
      "zipcode": "23505-1337",
      "geo": {
        "lat": "-71.4197",
        "lng": "71.7478"
      }
    },
    "phone": "1-477-935-8478 x6430",
    "website": "ola.org",
    "company": {
      "name": "Considine-Lockman",
      "catchPhrase": "Synchronised bottom-line interface",
      "bs": "e-enable innovative applications"
    }
  },
  {
    "id": 7,
    "name": "Kurtis Weissnat",
    "username": "Elwyn.Skiles",
    "email": "Telly.Hoeger@billy.biz",
    "address": {
      "street": "Rex Trail",
      "suite": "Suite 280",
      "city": "Howemouth",
      "zipcode": "58804-1099",
      "geo": {
        "lat": "24.8918",
        "lng": "21.8984"
      }
    },
    "phone": "210.067.6132",
    "website": "elvis.io",
    "company": {
      "name": "Johns Group",
      "catchPhrase": "Configurable multimedia task-force",
      "bs": "generate enterprise e-tailers"
    }
  },
  {
    "id": 8,
    "name": "Nicholas Runolfsdottir V",
    "username": "Maxime_Nienow",
    "email": "Sherwood@rosamond.me",
    "address": {
      "street": "Ellsworth Summit",
      "suite": "Suite 729",
      "city": "Aliyaview",
      "zipcode": "45169",
      "geo": {
        "lat": "-14.3990",
        "lng": "-120.7677"
      }
    },
    "phone": "586.493.6943 x140",
    "website": "jacynthe.com",
    "company": {
      "name": "Abernathy Group",
      "catchPhrase": "Implemented secondary concept",
      "bs": "e-enable extensible e-tailers"
    }
  },
  {
    "id": 9,
    "name": "Glenna Reichert",
    "username": "Delphine",
    "email": "Chaim_McDermott@dana.io",
    "address": {
      "street": "Dayna Park",
      "suite": "Suite 449",
      "city": "Bartholomebury",
      "zipcode": "76495-3109",
      "geo": {
        "lat": "24.6463",
        "lng": "-168.8889"
      }
    },
    "phone": "(775)976-6794 x41206",
    "website": "conrad.com",
    "company": {
      "name": "Yost and Sons",
      "catchPhrase": "Switchable contextually-based project",
      "bs": "aggregate real-time technologies"
    }
  },
  {
    "id": 10,
    "name": "Clementina DuBuque",
    "username": "Moriah.Stanton",
    "email": "Rey.Padberg@karina.biz",
    "address": {
      "street": "Kattie Turnpike",
      "suite": "Suite 198",
      "city": "Lebsackbury",
      "zipcode": "31428-2261",
      "geo": {
        "lat": "-38.2386",
        "lng": "57.2232"
      }
    },
    "phone": "024-648-3804",
    "website": "ambrose.net",
    "company": {
      "name": "Hoeger LLC",
      "catchPhrase": "Centralized empowering task-force",
      "bs": "target end-to-end models"
    }
  }
]
jsonData1 = json.dumps(dictData1)
dictData1 = json.loads(jsonData1)

@bot.message_handler(commands=['latlng'])
def latlng(message):
    first_element1 = dictData1[0]
    bot.send_message(message.chat.id,'Имя: ' + first_element1['name'] + "\nЛогин: " + dictData1[0]['username'] +
                     '\nТелефон: ' + dictData1[0]['phone'] + '\nСайт: ' + dictData1[0]['website'] +
                     '\nКомпания: ' + dictData1[0]['company']['name'])
    bot.send_chat_action(message.from_user.id, 'find_location')
    bot.send_location(message.chat.id, latitude=dictData1[0]['address']["geo"]["lat"],
                      longitude=dictData1[0]["address"]["geo"]["lng"])

@bot.message_handler(commands=['latlng1'])
def latlng1(message):
    first_element3 = dictData1[3]
    bot.send_message(message.chat.id,'Имя: ' + first_element3['name'] + "\nЛогин: " + dictData1[3]['username'] +
                     '\nТелефон: ' + dictData1[3]['phone'] + '\nСайт: ' + dictData1[3]['website'] +
                     '\nКомпания: ' + dictData1[3]['company']['name'])
    bot.send_chat_action(message.from_user.id, 'find_location')
    bot.send_location(message.chat.id, latitude=dictData1[3]['address']["geo"]["lat"],
                      longitude=dictData1[3]["address"]["geo"]["lng"])

@bot.message_handler(commands=['search_user'])
def search_user(message):
    name = 'Ervin Howell'
    results = f'Эмейл: ' + list(filter(lambda x: x['name'] == name, dictData1))[0]['email']
    bot.send_message(message.chat.id, results)

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
                                      f'👉🏻/latlng\n'
                                      f'Тест запроса JSON:\n'
                                      f'👉🏻/latlng1\n')

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
    elif message.text.lower() == 'ervin howell':
        name = 'Ervin Howell'
        results = f'Эмейл: ' + list(filter(lambda x: x['name'] == name, dictData1))[0]['email']
        bot.send_message(message.chat.id, results)
    elif message.text.lower() == 'ervin howel':
        name = 'Ervin Howell'
        results = f'Эмейл: ' + list(filter(lambda x: x['name'] == name, dictData1))[0]['email']
        bot.send_message(message.chat.id, results)
    elif message.text.lower() == 'ervin howe':
        name = 'Ervin Howell'
        results = f'Эмейл: ' + list(filter(lambda x: x['name'] == name, dictData1))[0]['email']
        bot.send_message(message.chat.id, results)
    else:
        bot.send_message(message.chat.id, f'Извини, {message.from_user.first_name}, но я тебя не понял.\n'
                                          f'За помощью - /help')



bot.polling(none_stop=True)