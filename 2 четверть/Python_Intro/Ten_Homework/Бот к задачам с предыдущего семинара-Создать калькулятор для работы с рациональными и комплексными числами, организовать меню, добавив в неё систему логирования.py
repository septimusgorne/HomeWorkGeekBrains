import telebot
from telebot import TeleBot
from telebot import types
from datetime import datetime as dt

TOKEN = "5543531310:AAEOV6jG5g37_0YA-eG01_lB43USwDYhxOo"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Calculator Online')
    key2 = types.KeyboardButton('Logger')
    key3 = types.KeyboardButton('Clear_log')

    kboard.add(key1, key2, key3)

    bot.send_message(message.chat.id, '** {0.first_name}, добро пожаловать в MyCalcOnline **'.format(
        message.from_user), reply_markup=kboard)


@bot.message_handler(content_types=['text'])
def bot_menu(message):
    time = dt.now().strftime('%H:%M')
    user = message.from_user.first_name
    user_id = str(message.from_user.id)
    text = message.text

    with open('logger.txt', 'a', encoding='UTF-8') as data:
        log_input = ' '.join([time, user, user_id, text])
        data.write(f'{log_input}\n')

    if message.text == 'Calculator Online':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Back to Main Menu')
        kboard.add(back)

        bot.send_message(message.chat.id, 'Что хотите посчитать? Введите выражение: ',
                         reply_markup=kboard)

    elif message.text == 'Logger':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Back to Main Menu')
        kboard.add(back)
        bot.send_message(message.chat.id, 'Bot_Log...',
                         reply_markup=kboard)
        with open('logger.txt', 'r', encoding='UTF-8') as db:
            db_out = db.readlines()
            for line in db_out:
                bot.send_message(message.chat.id, {line})

    elif message.text == 'Clear_log':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y = types.KeyboardButton('yes')
        n = types.KeyboardButton('no')
        kboard.add(y, n)
        bot.send_message(message.chat.id, 'Clear log info? Are you sure?',
                         reply_markup=kboard)

    elif message.text == 'no':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Calculator Online')
        key2 = types.KeyboardButton('Logger')
        key3 = types.KeyboardButton('Clear_log')

        kboard.add(key1, key2, key3)

        bot.send_message(message.chat.id, 'Clear_log canceled, back to main menu',
                         reply_markup=kboard)

    elif message.text == 'yes':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Calculator Online')
        key2 = types.KeyboardButton('Logger')
        key3 = types.KeyboardButton('Clear_log')

        kboard.add(key1, key2, key3)

        bot.send_message(message.chat.id, 'Log_cleared, back to main menu',
                         reply_markup=kboard)

        log_renew = open('logger.txt', 'w', encoding='UTF-8')
        log_renew.close()

    elif message.text == 'Back to Main Menu':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Calculator Online')
        key2 = types.KeyboardButton('Logger')
        key3 = types.KeyboardButton('Clear_log')

        kboard.add(key1, key2, key3)

        bot.send_message(message.chat.id, '** {0.first_name}, добро пожаловать в MyCalcOnline **'.format(
            message.from_user), reply_markup=kboard)

    else:
        try:
            value = eval(message.text)
            bot.send_message(message.chat.id, f'{message.text} = {value}')
        except:
            bot.send_message(
                message.chat.id, 'Не могу посчитать такое, попробуй что-то еще: ')


if __name__ == '__main__':
    bot.infinity_polling()
