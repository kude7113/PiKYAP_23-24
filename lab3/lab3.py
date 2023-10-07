import sqlite3
import telebot
import random
from matplotlib import pyplot as plt
from io import BytesIO
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
        piska = 0
        time = message.date
        cur.execute('SELECT * FROM piski')
        piski = cur.fetchall()
        i = 0
        for el in piski:
            if chat_id == el[1] and user_id == el[2]:
                i += 1
        if i == 0:
            cur.execute("INSERT INTO piski (id_chat, id_user, piska, name, dat) VALUES ('%d', '%d','%d', '%s', '%d')" % (chat_id, user_id, piska, user_name, time))

        cur.execute("SELECT * FROM piski WHERE id_chat == '%d' AND id_user == '%d'" % (chat_id, user_id))
        user_info = cur.fetchone()
        int_dat = user_info[5]
        now_pisun = user_info[3]

        if time - int_dat > 10 or i == 0:
            rand = random.randint(-5, 10)
            now_pisun += rand
            cur.execute("UPDATE piski SET piska = piska + '%d' WHERE id_chat == '%d' AND id_user == '%d'" % (
            rand, chat_id, user_id))
            cur.execute(
                "UPDATE piski SET dat = '%d' WHERE id_chat == '%d' AND id_user == '%d'" % (time, chat_id, user_id))
            q = ''
            if rand > 0:
                q = user_name + ' ваша писька выросла на ' + str(rand) + ' см' + '\n' + 'Теперь ваш писюн: ' + str(now_pisun)
            else:
                q = user_name + ' ваша писька сократилась на ' + str(abs(rand)) + ' см' + '\n' + 'Теперь ваш писюн: ' + str(now_pisun)
            bot.send_message(message.chat.id, q)
        else:
            bot.send_message(message.chat.id, 'Этой командой можно пользоваться раз в 24 часа!')
        conn.commit()
        cur.close()
        conn.close()

    else:
        bot.send_message(message.chat.id, 'Этой командой можно пользоваться только в группах')


@bot.message_handler(commands = ['top_pisun'])
def main(message):
    chat_id = message.chat.id
    conn = sqlite3.connect('piski.sql')
    cur = conn.cursor()
    cur.execute("SELECT * FROM piski WHERE id_chat == '%d'" % (chat_id))
    piski = cur.fetchall()
    top = []
    for el in piski:
        top.append([el[3], el[4]])
    top.sort()
    p = ''
    for i in range(len(top)):
        p += str(i + 1) + ') ' +str(top[i][1]) + ' - ' + str(top[i][0]) + 'см' + '\n'
        bot.send_message(message.chat.id, p)
    if top == []:
        bot.send_message(message.chat.id, 'У всех в этом чате письки равны 0')

@bot.message_handler(commands = ['diagrama'])
def main(message):
    chat_id = message.chat.id
    conn = sqlite3.connect('piski.sql')
    cur = conn.cursor()
    cur.execute("SELECT * FROM piski WHERE id_chat == '%d'" % (chat_id))
    piski = cur.fetchall()
    top = []
    for el in piski:
        top.append([el[3], el[4]])
    top.sort()
    dick = []
    name = []
    for i in range(len(top)):
        dick.append(top[i][0])
        name.append(top[i][1])
    data = [20, 30, 50]
    labels = ['Категория 1', 'Категория 2', 'Категория 3']

    # Создаем круговую диаграмму
    plt.figure(figsize=(6, 6))
    plt.pie(dick, labels=name, autopct='%1.1f%%')
    plt.title('Пример диаграммы')

    # Сохраняем диаграмму во временный файл
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Отправляем диаграмму в чат
    bot.send_photo(message.chat.id, photo=buf)

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
