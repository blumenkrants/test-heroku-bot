import logging
from glob import glob
# import ephem
from random import choice
from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

TOKEN ='706281842:AAEfTA463zVG9UBQp6g-AbZOcT1DLIctZc0'


USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# def planet (bot, update):
#     text1 = 'Вызван /planet Mars'
#     print('Mars')
#
#     planet_name = text1.split()[2]
#     if planet_name == "Mars":
#         mars1 = ephem.Mars('2018/11/30')
#         print(update.message.reply_text(ephem.constellation(mars1)))
# Функция платнеты

# def send_fighter_picture (bot, update):
#     fight_list = glob("/Users/dmitriy/Downloads/fighters*.jp*g")
#     fight_pic = choice(fight_list)
#     bot.send_photo(chat_id=update.message.chat.id, photo=open(fight_pic, 'rb'))
# # Функция фотки

def send_fighter_picture (bot, update):
    text = 'This is Heroku!'
    my_keyboard = ReplyKeyboardMarkup([['/fighters', '/start']], resize_keyboard=True)
    update.message.reply_text(text, reply_markup=my_keyboard)


def greet_user(bot, update):
    smile = emojize(choice(USER_EMOJI), use_aliases=True)
    text = 'Привет {}'.format(smile)
    contact_button = KeyboardButton('Контактные данные', request_contact=True)
    location_button = KeyboardButton('Геолокация', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([['/fighters'], [contact_button, location_button]], resize_keyboard=True)
    print("привет")
    update.message.reply_text(text, reply_markup=my_keyboard)

def get_contact(bot, update):
    print(update.message.contact)
    update.message.reply_text('Спасибо')

def get_location(bot, update):
    print(update.message.location)
    update.message.reply_text('Спасибо')

def wordcount(bot, update): 
    q = update.message.text .split()
    a = (len(q))
    update.message.reply_text(str(a - 1) + " words") 

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)    

def main():
    mybot = Updater("706281842:AAEfTA463zVG9UBQp6g-AbZOcT1DLIctZc0", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    # dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("wordcount", wordcount))

    #меняет название кнопки
    # dp.add_handler(RegexHandler('^(Показать бойца UFC)$', send_fighter_picture)) 
       
    dp.add_handler(CommandHandler("fighters", send_fighter_picture))
    dp.add_handler(MessageHandler(Filters.contact, get_contact))
    dp.add_handler(MessageHandler(Filters.location, get_location))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()