import datetime
import time

import telebot
from telebot.types import Message

from scripts.work_with_user_id import add_user, read_user_set, get_user_massives
from keyboards import main_keyboard
from scripts.print_months import THIS_M, NEXT_M, send_alert
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    add_user(message)
    message_alert = send_alert()
    users_massive = get_user_massives()
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}!\n'
                                      'С моей помощью, ты сможешь следить за фазами Луны,\n'
                                      'Для начала работы, выберите МЕНЮ.\n', reply_markup=keyboard)


keyboard = main_keyboard()


@bot.message_handler(content_types=['text'])
def send_answer(message: Message):
    text = message.text
    if text == '❓ Луна сегодня':
        bot.send_message(message.chat.id, '🌖 Сегодня убывающая луна', reply_markup=keyboard)
    elif text == '▶️ В этом месяце':
        bot.send_message(message.chat.id, THIS_M, reply_markup=keyboard)
    elif text == '⏩ В следующем месяце':
        bot.send_message(message.chat.id, NEXT_M, reply_markup=keyboard)
    elif message.text == 'Статистика':
        answer = read_user_set()
        bot.send_message(
            message.chat.id,
            text=answer,
            reply_markup=keyboard,
        )


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            time.sleep(3)
            print(ex)
