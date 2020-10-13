import telebot
from telebot.types import Message

from settings import TOKEN
from keyboards import main_keyboard
from scraper import phase_text

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Сегодня убывающая луна', reply_markup=keyboard)


keyboard = main_keyboard()


@bot.message_handler(content_types=['text'])
def send_answer(message: Message):
    text = message.text

    if text == '❓ Луна сегодня':
        bot.send_message(message.chat.id, '🌖 Сегодня убывающая луна', reply_markup=keyboard)

    elif text == '🌕 Полнолуния и 🌑 Новолуния':
        bot.send_message(message.chat.id, phase_text, reply_markup=keyboard)


bot.polling()