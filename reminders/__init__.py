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
        request = "CREATE TABLE IF NOT EXISTS total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, text TEXT, date_until TEXT)"
        self.cur.execute(request)
    def __enter__(self):
        self.con = sqlite3.connect("dbs/tasks.db")
        self.cur = self.con.cursor()
        request = "CREATE TABLE IF NOT EXISTS total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, text TEXT, date_until TEXT)"
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
    def read_all(self):
        """
        Reads all tasks\n
        Считывает все напоминания.
        """
        request = "SELECT * FROM total_tasks"
        self.cur.execute(request)
        self.commit()
        return self.cur.fetchall()
    def con_exit(self):
        """
        Closes the connection\n
        Закрывает соединение.
        """
        self.con.close()
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