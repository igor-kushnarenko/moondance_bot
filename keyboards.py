import telebot


def main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('❓ Луна сегодня')
    keyboard.row('🌕 Следующее полнолуние')
    keyboard.row('🌑 Следующее новолуние')
    return keyboard