import sqlite3
import telebot
import random
from telebot import types

bot = telebot.TeleBot('5782807787:AAEcV-5TiSrSzY-vM5i05HAn9o7aYCwRHzc')

conn = sqlite3.connect('piski.sql')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS piski (id int auto_increment pimary key,id_chat int, id_user int, piska int, name varchar(50))')
conn.commit()
cur.close()
conn.close()

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands = ['pisun'])
def main(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_name = message.from_user.username
        piska = 0
        conn = sqlite3.connect('piski.sql')
        cur = conn.cursor()

        cur.execute('SELECT * FROM piski')
        piski = cur.fetchall()
        i = 0
        for el in piski:
            if chat_id == el[1] and user_id == el[2]:
                i += 1
                u = random.randint(-5, 10)
                cur.execute("UPDATE piski SET piska = piska + '%d' WHERE id_chat == '%d' AND id_user == '%d'" % (u, chat_id, user_id))
                q = ''
                if u > 0:
                    q = user_name + ' ваша писька выросла на ' + str(u) + ' см'
                else:
                    q = user_name + ' ваша писька сократилась на ' + str(abs(u)) + ' см'
                bot.send_message(message.chat.id, q)
        if i == 0:
            cur.execute("INSERT INTO piski (id_chat, id_user, piska, name) VALUES ('%d', '%d','%d', '%s')" % (chat_id, user_id, piska, user_name))

        conn.commit()
        cur.close()
        conn.close()

    else:
        bot.send_message(message.chat.id, 'Этой командой можно пользоваться только в группах')

@bot.message_handler(commands = ['print'])
def main(message):
    conn = sqlite3.connect('piski.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM piski')
    piski = cur.fetchall()

    info = ''
    for el in piski:
        info += f'chat_id: {el[1]}, user_id: {el[2]}, piska: {el[3]}, name: {el[4]}\n'
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, info)


bot.polling(none_stop=True)
