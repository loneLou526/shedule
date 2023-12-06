import telebot
import sqlite3 as sl
from datetime import date
import calendar
from db import DB_shed
import schedule
from time import sleep
from threading import Thread
 
with open('token.txt', 'r') as f:
    bot = telebot.TeleBot(f.read())
db = DB_shed()

@bot.message_handler(commands=['start'])
def start(mes):
    bot.send_message(mes.chat.id, db.insert_user(mes.chat.id, mes.chat.title))

def send_shedule():
    try:
        con = sl.connect('schedule.db')
        cur = con.cursor()
        day = date.today()
        cur.execute(f"""
                    SELECT id, subjects, time FROM {calendar.day_name[day.weekday()]}
                    """)
        data = [f'{i[0]}) {i[1]}\n{i[2]}\n\n' for i in cur.fetchall()]
        return bot.send_message(db.get_usID(), ''.join(data))
    except:
        return bot.send_message(db.get_usID(), 'Либо я полетел, либо сегодня нет уроков.\nВ любом случае кайфуйте.')

# schedule.every().day.at("18:13").do(send_shedule)

# bot.polling(none_stop=True, interval=0)
def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == '__main__':
    schedule.every().day.at("18:33").do(send_shedule)
    Thread(target=schedule_checker).start()  
    # server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
