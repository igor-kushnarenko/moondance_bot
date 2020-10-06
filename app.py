import telebot
from telebot.types import Message

from settings import TOKEN
from keyboards import main_keyboard

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

    elif text == '🌕 Следующее полнолуние':
        bot.send_message(message.chat.id, 'Следующее полнолуние 31 октября в 14:49', reply_markup=keyboard)

    elif text == '🌑 Следующее новолуние':
        bot.send_message(message.chat.id, 'Следующее новолуние 16 октября в 19:30', reply_markup=keyboard)





bot.polling()