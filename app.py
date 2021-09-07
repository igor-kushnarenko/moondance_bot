import time

import telebot
from telebot.types import Message

from scripts.work_with_user_id import add_user, read_user_set
from scripts.scraper import phase_text_this_month, phase_text_next_month
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('▶️ В этом месяце')
keyboard.row('⏩ В следующем месяце')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    add_user(message)
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}!\n'
                                      'С моей помощью, ты сможешь следить за фазами Луны,\n'
                                      'Для начала работы, выберите МЕНЮ.\n', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_answer(message: Message):
    text = message.text
    if text == '❓ Луна сегодня':
        bot.send_message(message.chat.id, '🌖 Сегодня убывающая луна', reply_markup=keyboard)
    elif text == '▶️ В этом месяце':
        bot.send_message(message.chat.id, phase_text_this_month, reply_markup=keyboard)
    elif text == '⏩ В следующем месяце':
        bot.send_message(message.chat.id, phase_text_next_month, reply_markup=keyboard)
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
