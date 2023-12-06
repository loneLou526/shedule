import sqlite3 as sl
from datetime import date, datetime
import calendar
from time import sleep
con = sl.connect('schedule.db')

cur = con.cursor()
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# for i in days:
#     cur.execute(f"""DROP TABLE {i}""")
# cur.execute("""
#             CREATE TABLE Sunday(
#                 id INTEGER PRIMARY KEY,
#                 subjects TEXT,
#                 time TEXT,
#                 start_date TEXT,
#                 end_date TEXT
#             )""")
cur.execute("""DELETE FROM Sunday""")
con.commit()
# day = date.today()
# cur.execute("""SELECT id FROM Thursday""")
# # print(cur.fetchone()[0])
# cur.execute(f"""SELECT id, subjects, time FROM {calendar.day_name[day.weekday()]}""")
# data = [f'{i[0]}) {i[1]}\n{i[2]}\n\n' for i in cur.fetchall()]
# print(''.join(data))
# while True:
#     sleep(1)
#     if datetime.now().time().strftime("%H:%M:%S") == '02:10:35':
#         print('Hello')
        
    # else:
    #     print('None')
# print(datetime.now().time().strftime("%H:%M:%S"))
