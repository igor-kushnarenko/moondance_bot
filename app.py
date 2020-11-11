import telebot
from telebot.types import Message
import datetime
import time

from settings import TOKEN
from keyboards import main_keyboard
from print_months import THIS_M, NEXT_M

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Приветствую тебя дорогой друг!\n'
                                      'С моей помощью, ты сможешь следить за фазами Луны,\n'
                                      'Для начала работы, выберите МЕНЮ.\n', reply_markup=keyboard)
    while True:
        times = datetime.datetime.now().strftime('%H:%M')
        if times == '10:23':
            if day_x:
                bot.send_message(message.from_user.id, 'ALERT!!!!!!')
        time.sleep(60)


keyboard = main_keyboard()


@bot.message_handler(content_types=['text'])
def send_answer(message: Message):
    text = message.text

    if text == '❓ Луна сегодня':
        bot.send_message(message.chat.id, '🌖 Сегодня убывающая луна', reply_markup=keyboard)

    elif text == '🌕 В этом месяце 🌑':
        bot.send_message(message.chat.id, THIS_M, reply_markup=keyboard)

    elif text == '🌕 В следующем месяце 🌑':
        bot.send_message(message.chat.id, NEXT_M, reply_markup=keyboard)


bot.polling()