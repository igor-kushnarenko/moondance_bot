import telebot


def main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('❓ Луна сегодня')
    keyboard.row('🌕 Полнолуния и 🌑 Новолуния')
    return keyboard