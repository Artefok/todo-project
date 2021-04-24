import sqlite3
con = sqlite3.connect("tasks.db")
cur = con.cursor()
request = "CREATE TABLE IF NOT EXISTS total_tasks(id, date, text)"
cur.execute(request)
def create_a_task(date_exec, text_exec):
    """
    Creates a task.
    """
    request = "INSERT INTO total_tasks(date, text) VALUES(?, ?)"
    cur.execute(request, (date_exec, text_exec))
    con.commit()
def delete_the_task(task_id):
    """
    Deletes the task
    """
    request = "DELETE FROM total_tasks WHERE id = ?"
    cur.execute(request, task_id)
    con.commit()
def read_one_id(task_id):
    """
    Reads the task. Requires task id
    """
    request = "SELECT * FROM total_tasks WHERE id = ?"
    cur.execute(request, task_id)
    con.commit()
    return cur.fetchall()
def read_one_day(date):
    """
    Reads the tasks on one day
    """
    request = "SELECT * FROM total_tasks WHERE date = ?"
    cur.execute(request, date)
    con.commit()
    return cur.fetchall()
def read_all():
    """
    Reads all tasks
    """
    request = "SELECT * FROM total_tasks"
    cur.execute(request)
    con.commit()
    return cur.fetchall()
def clear():
    request = "DROP TABLE IF EXISTS total_tasks"
    cur.execute(request)
    request = "CREATE TABLE total_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, text TEXT)"
    cur.execute(request)
def con_exit():
    """
    Closes the connection
    """
    con.close()