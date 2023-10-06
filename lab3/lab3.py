import telebot

bot = telebot.TeleBot('5782807787:AAEcV-5TiSrSzY-vM5i05HAn9o7aYCwRHzc')

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands = ['dick'])
def main(user):
    if user.chat.type == 'private':
        bot.send_message(user.chat.id, 'Этой командой можно пользоваться только в группах')
    else:
        bot.send_message(user.chat.id, 'у тебя большая писька')

bot.polling(none_stop=True)
