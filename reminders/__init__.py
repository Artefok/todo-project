"""
This module implements reminder system\
Этот модуль реализовывает систему напоминаний.
"""
import sqlite3
class run:
    def __init__(self, path="dbs/tasks.db"):
        """
        Connects to the database\n
        Подключается к базе данных
        """
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        request = "CREATE TABLE IF NOT EXISTS total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, text TEXT, date_until TEXT, task_id INTEGER)"
        self.cur.execute(request)
    def __enter__(self):
        self.con = sqlite3.connect("dbs/tasks.db")
        self.cur = self.con.cursor()
        request = "CREATE TABLE IF NOT EXISTS total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, text TEXT, date_until TEXT, task_id INTEGER)"
        self.cur.execute(request)
        return (self.con, self.cur)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()
        if exc_val:
            raise Exception
    def create_a_task(self, date_exec, text_exec, date_until, task_id, name=None):
        """
        Creates a task.\n
        Создаёт напоминание.
        """
        if not name:
            name = "notnamed"
        request = "INSERT INTO total_tasks(name, date, text, date_until, task_id) VALUES(?, ?, ?, ?, ?)"
        self.cur.execute(request, (name, date_exec, text_exec, date_until, task_id))
        self.commit()
    def delete_the_task(self, task_id):
        """
        Deletes the task. Requires task id\n
        Удаляет напоминание. Требуется идентификатор напоминания.
        """
        request = "DELETE FROM total_tasks WHERE id = ?"
        self.cur.execute(request, (task_id,))
        self.commit()
    # region
    # def read_one_id(self, task_id):
    #     """
    #     Reads the task. Requires task id\n
    #     Считывает напоминание. Требуется идентификатор напоминания.
    #     """
    #     request = "SELECT * FROM total_tasks WHERE id = ?"
    #     self.cur.execute(request, (task_id,))
    #     self.commit()
    #     return self.cur.fetchall()
    # def read_one_day(self, date):
    #     """
    #     Reads the tasks on one day\n
    #     Считывает напоминание на определённый день.
    #     """
    #     request = "SELECT * FROM total_tasks WHERE date = ?"
    #     self.cur.execute(request, (date,))
    #     self.commit()
    #     return self.cur.fetchall()
    #endregion
    def read_all(self):
        """
        Reads all tasks\n
        Считывает все напоминания.
        """
        request = "SELECT * FROM total_tasks"
        self.cur.execute(request)
        self.commit()
        return self.cur.fetchall()
    # region
    # def clear(self):
    #     """
    #     Clears everything\n
    #     Очищает базу данных.
    #     """
    #     request = "DROP TABLE IF EXISTS total_tasks"
    #     self.cur.execute(request)
    #     request = "CREATE TABLE IF NOT EXISTS total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, text TEXT, date_until TEXT)"
    #     self.cur.execute(request)
    #endregion
    def con_exit(self):
        """
        Closes the connection\n
        Закрывает соединение.
        """
        self.con.close()
    # region
    # def show_on_date(self, date):
    #     """
    #     Returns every reminder on date\n
    #     Возвращает каждое напоминание на определённый день.
    #     """
    #     return self.read_one_day(date)
    # def __get_today(self):
    #     """
    #     Returns today as date\n
    #     Возвращает дату сегодняшнего дня.
    #     """
    #     date = f"{localtime(time()).tm_year}-{localtime(time()).tm_mon}-{localtime(time()).tm_mday}"
    #     return date
    # def show_today(self):
    #     """
    #     Returns every reminder today\n
    #     Возвращает каждое напоминание на сегодня.
    #     """
    #     date = self.__get_today()
    #     return self.read_one_day(date)
    # def reminder(self):
    #     """
    #     Prints today's reminders\n
    #     Печатает напоминания на сегодня.
    #     """
    #     for i in self.show_today():
    #         print(f"id{i[0]}  {i[1]} from {i[2]} to {i[4]}.{i[5]}: {i[3]}")
    #         print(f"id{i[0]}  {i[1]} с {i[2]} до {i[4]}.{i[5]}: {i[3]}")
    # def reminder_on_date(self, date):
    #     """
    #     Prints date's reminders\n
    #     Печатает напоминания на определённый день.
    #     """
    #     try:
    #         for i in self.show_on_date(date):
    #             print(f"id{i[0]} {i[1]} from {i[2]} to {i[4]}.{i[5]}: {i[3]}")
    #             print(f"id{i[0]} {i[1]} с {i[2]} до {i[4]}.{i[5]}: {i[3]}")
    #     except Exception as err:
    #         print(err)
    # def reminder_all(self):
    #     """
    #     Prints all reminders\n
    #     Печатает все напоминания.
    #     """
    #     try:
    #         for i in self.read_all():
    #             print(f"id{i[0]} {i[1]} from {i[2]} to {i[4]}.{i[5]}: {i[3]}")
    #             print(f"id{i[0]} {i[1]} с {i[2]} до {i[4]}.{i[5]}: {i[3]}")
    #     except Exception as err:
    #         print(err)
    #endregion
    def update(self, date_until, text, task_id, date_exec, display_id, name=None):
        """
        Updates reminder\n
        Обновление напоминания
        """
        if not name:
            name = "notnamed"
        request = "UPDATE total_tasks SET date_until=?, text=?, name=?, date=?, task_id=? WHERE id=?"
        self.cur.execute(request, (date_until, text, name, date_exec, display_id, task_id))
        self.commit()
    def commit(self):
        self.con.commit()
__all__ = ["run", "sqlite3"]