# -*- coding: utf-8 -*-

import json

import apiai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

REQUEST_KWARGS = {'proxy_url': 'http://13.57.194.21:3128'}
updater = Updater(token='794660132:AAETmCoAhTHGyH6rU3VNxLpbDCkVRWp5YpM', request_kwargs=REQUEST_KWARGS)  # Токен бота
dispatcher = updater.dispatcher


# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='/Стоп')


def textMessage(bot, update):
    try:
        request = apiai.ApiAI('84095557c4114b78aba506850602c83f').text_request()  # Токен API к Dialogflow
        request.lang = 'ru'  # На каком языке будет послан запрос
        request.session_id = 'JohnBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
        request._time_zone = 'utc'
        request.query = update.message.text
        resp = request.getresponse().read().decode('utf-8')
        responseJson = json.loads(resp)
        response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
        if response:
            bot.send_message(chat_id=update.message.chat_id, text=response)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Че?')
    except Exception, e:
        bot.send_message(chat_id=update.message.chat_id, text=e)


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
