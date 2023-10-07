import sqlite3
import telebot
import random

bot = telebot.TeleBot('5782807787:AAEcV-5TiSrSzY-vM5i05HAn9o7aYCwRHzc')

conn = sqlite3.connect('piski.sql')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS piski (id int auto_increment pimary key,id_chat int, id_user int, piska int, name varchar(50),dat int)')
conn.commit()
cur.close()
conn.close()

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands = ['pisun'])
def main(message):
    conn = sqlite3.connect('piski.sql')
    cur = conn.cursor()
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_name = message.from_user.username
        time = message.date
        piska = 0
        cur.execute('SELECT * FROM piski')
        piski = cur.fetchall()
        i = 0
        for el in piski:
            if chat_id == el[1] and user_id == el[2]:
                cur.execute("SELECT * FROM piski WHERE id_chat == '%d' AND id_user == '%d'" % (chat_id, user_id))
                user_info = cur.fetchone()
                int_dat = user_info[5]
                if message.date - int_dat < 86400:
                    bot.send_message(message.chat.id, 'Эту команду можно использовать раз в 24 часа')
                    break
                else:
                    i += 1
                    rand = random.randint(-5, 10)
                    cur.execute("UPDATE piski SET piska = piska + '%d' WHERE id_chat == '%d' AND id_user == '%d'" % (rand, chat_id, user_id))
                    q = ''
                    if rand > 0:
                        q = user_name + ' ваша писька выросла на ' + str(rand) + ' см'
                    else:
                        q = user_name + ' ваша писька сократилась на ' + str(abs(rand)) + ' см'
                    bot.send_message(message.chat.id, q)
        if i == 0:
            cur.execute("INSERT INTO piski (id_chat, id_user, piska, name, dat) VALUES ('%d', '%d','%d', '%s', '%d')" % (chat_id, user_id, piska, user_name, time))

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
        info += f'chat_id: {el[1]}, user_id: {el[2]}, piska: {el[3]}, name: {el[4]}, time: {el[5]}\n'
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, info)


bot.polling(none_stop=True)
