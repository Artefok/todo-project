"""
This module implements reminder system\
Этот модуль реализовывает систему напоминаний.
"""
import sqlite3
import time
import os
class run:
    def __init__(self, path, ctx=False):
        """
        Connects to the database\n
        Подключается к базе данных
        """
        if not ctx:
            self.con = sqlite3.connect(path)
            self.cur = self.con.cursor()
            request = "CREATE TABLE IF NOT EXISTS total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name, date, text, date_until)"
            self.cur.execute(request)
    def __enter__(self):
        self.con = sqlite3.connect("dbs/tasks.db")
        self.cur = self.con.cursor()
        request = "CREATE TABLE IF NOT EXISTS total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name, date, text, date_until)"
        self.cur.execute(request)
        return (self.con, self.cur)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()
        if exc_val:
            raise
    def create_a_task(self, date_exec, text_exec, name=None, date_until=None):
        """
        Creates a task.\n
        Создаёт напоминание.
        """
        request = "INSERT INTO total_tasks(date, text) VALUES(?, ?, ?, ?)"
        self.cur.execute(request, (name, date_exec, text_exec, date_until))
        self.con.commit()
    def delete_the_task(self, task_id):
        """
        Deletes the task. Requires task id\n
        Удаляет напоминание. Требуется идентификатор напоминания.
        """
        request = "DELETE FROM total_tasks WHERE id = ?"
        self.cur.execute(request, (task_id,))
        self.con.commit()
    def read_one_id(self, task_id):
        """
        Reads the task. Requires task id\n
        Считывает напоминание. Требуется идентификатор напоминания.
        """
        request = "SELECT * FROM total_tasks WHERE id = ?"
        self.cur.execute(request, (task_id,))
        self.con.commit()
        return self.cur.fetchall()
    def read_one_day(self, date):
        """
        Reads the tasks on one day\n
        Считывает напоминание на определённый день.
        """
        request = "SELECT * FROM total_tasks WHERE date = ?"
        self.cur.execute(request, (date,))
        self.con.commit()
        return self.cur.fetchall()
    def read_all(self):
        """
        Reads all tasks\n
        Считывает все напоминания.
        """
        request = "SELECT * FROM total_tasks"
        self.cur.execute(request)
        self.con.commit()
        return self.cur.fetchall()
    def clear(self):
        """
        Clears everything\n
        Очищает базу данных.
        """
        request = "DROP TABLE IF EXISTS total_tasks"
        self.cur.execute(request)
        request = "CREATE TABLE total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name, date, text, date_until)"
        self.cur.execute(request)
    def con_exit(self):
        """
        Closes the connection\n
        Закрывает соединение.
        """
        self.con.close()
    def show_on_date(self, date):
        """
        Returns every reminder on date\n
        Возвращает каждое напоминание на определённый день.
        """
        return self.read_one_day(date)
    def __get_today(self):
        """
        Returns today as date\n
        Возвращает дату сегодняшнего дня.
        """
        date = f"{time.localtime(time.time()).tm_year}-{time.localtime(time.time()).tm_mon}-{time.localtime(time.time()).tm_mday}"
        return date
    def show_today(self):
        """
        Returns every reminder today\n
        Возвращает каждое напоминание на сегодня.
        """
        date = self.__get_today()
        return self.read_one_day(date)
    def reminder(self):
        """
        Prints today's reminders\n
        Печатает напоминания на сегодня.
        """
        for i in self.show_today():
            print(f"{i[1]} from {i[2]} to {i[4]}: {i[3]}")
            print(f"{i[1]} с {i[2]} до {i[4]}: {i[3]}")
    def reminder_on_date(self, date):
        """
        Prints date's reminders\n
        Печатает напоминания на определённый день.
        """
        try:
            for i in self.show_on_date(date):
                print(f"{i[1]} from {i[2]} to {i[4]}: {i[3]}")
                print(f"{i[1]} с {i[2]} до {i[4]}: {i[3]}")
        except Exception as err:
            print(err)
    def reminder_all(self, date):
        """
        Prints all reminders\n
        Печатает все напоминания.
        """
        try:
            for i in self.read_all(date):
                print(f"{i[1]} from {i[2]} to {i[4]}: {i[3]}")
                print(f"{i[1]} с {i[2]} до {i[4]}: {i[3]}")
        except Exception as err:
            print(err)
    def update(self, date_until, text, task_id, name=None):
        """
        Updates reminder\n
        Обновление напоминания
        """
        request = "UDPATE total_tasks SET date_until=?, text=?, name=? WHERE id=?"
        self.cur.execute(request, (date_until, text, name, task_id))
        self.con.commit()