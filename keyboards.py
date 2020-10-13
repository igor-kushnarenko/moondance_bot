import telebot


def main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('❓ Луна сегодня')
    keyboard.row('🌕 В этом месяце 🌑')
    keyboard.row('🌕 В следующем месяце 🌑')
    return keyboard