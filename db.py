import sqlite3 as sl

class DB_shed():
    def get_usID():
        try:
            con = sl.connect('schedule.db')
            cur = con.cursor()

            cur.execute("""SELECT id FROM id_us""")
            print(cur.fetchone()[0])
            return cur.fetchone()[0]
        except sl.Error as ex:
            print('SQLite ERROR', ex)
        finally:
            if con:
                cur.close()
                con.close()        
    def insert_user(self, id, name):
        try:
            con = sl.connect('schedule.db')
            cur = con.cursor()
            cur.execute("SELECT name FROM id_us WHERE id = ?", (id,))
            if not cur.fetchone():
                cur.execute("""
                            INSERT INTO id_us VALUES (?, ?)
                            """, (id, name))
                con.commit()
                return 'Я успешно добавлен в вашу группу. Теперь каждое утро я буду скидвать вам ваше расписание, чтоб вы понимали какой пиздец ваш ждет сегодня. Удачи.'
            return 'Я прекрасно работаю, и вы уже есть в базе данных, так что хватит тыкать на кнопку start!!!'
        except sl.Error as ex:
            print('SQLite ERROR', ex)
            return 'Произошла какая-то ошибка, мы с этим уже работаем.'
        finally:
            if con:
                cur.close()
                con.close()    

    def creat_table(self):
        try:
            con = sl.connect('schedule.db')
            cur = con.cursor()
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            for day in days:
                cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS {day}(
                            id INTEGER PRIMARY KEY,
                            subjects TEXT,
                            time TEXT,
                            start_date TEXT,
                            end_date TEXT
                    )
                        """)
            con.commit()
        except sl.Error as ex:
            print('SQLite ERROR', ex)
        finally:
            if con:
                cur.close()
                con.close()
    
    def insert_db(self, table_name, sub_name, time, st_date, end_date):
        try:
            con = sl.connect('schedule.db')
            cur = con.cursor()
            
            cur.execute(f"""
                INSERT INTO {table_name} (subjects, time, start_date, end_date) VALUES (?, ?, ?, ?)""", (sub_name, time, st_date, end_date))
            con.commit()    

            return 'Данные добавлены'
        
        except sl.Error as ex:
            print('SQLite ERROR', ex)
        finally:
            if con:
                cur.close()
                con.close()



# db = DB_shed()
# data = {
#     'tototo': '8:30 - 10:10/10:20 - 12:00',
#     'Информатика (Каб. 0308)': '12:20 - 14:00',
#     'Русский язык и культура речи (Каб. 0209)': '14:10 - 15:50'
#         }

# for sub in data:
#     db.insert_db('Sunday', sub, data[sub], None, None)
# db.creat_table()
 