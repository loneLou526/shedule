import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import sqlite3 as sl
from datetime import date, datetime
import calendar
from db import DB_shed
from time import sleep

logging.basicConfig(level=logging.INFO)
with open('token.txt', 'r') as TOKEN:
    bot = Bot(token=TOKEN.read())

db = DB_shed()
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(db.insert_user(message.chat.id, message.chat.title))

# @dp.message(Command("shed"))
async def send_schedule():
    try:
        con = sl.connect('schedule.db')
        cur = con.cursor()
        day = date.today()
        cur.execute(f"""
                    SELECT id, subjects, time FROM {calendar.day_name[day.weekday()]}
                    """)
        data = [f'{i[0]}) {i[1]}\n{i[2]}\n\n' for i in cur.fetchall()]
        await bot.send_message(chat_id='-1001880703976', text=f"Ваше расписание на сегодня:\n{''.join(data)}")
    except sl.Error as ex:
        print(ex)
        await bot.send_message(chat_id='-1001880703976', text='Произошла какая-то ошибка, но она уже исправляется.')

# async def test():
#     await bot.send_message(chat_id='-1001880703976', text='Hello')


async def send_mes():
    while True:
        print(2)
        sleep(1)
        if datetime.now().time().strftime("%H:%M:%S") == '02:47:45':
            await send_schedule()

# async def scheduler_job():
#     scheduler.add_job(mes, 'interval', seconds=5, args=(dp,))

# async def scheduler():
#     aioschedule.every(5).seconds.do(mes)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

# async def on_startup(dp): 
#     print(1)
#     asyncio.create_task(scheduler())


async def main():
    # await scheduler_job()
    await dp.start_polling(bot)

if __name__ == "__main__":
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.create_task(send_mes())
    loop.run_forever()
  