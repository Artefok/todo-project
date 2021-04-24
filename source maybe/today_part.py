import db_part
import time
def show_on_date(date):
    return db_part.read_one_day((date,))

def get_today():
    date = f"{time.localtime(time.time()).tm_year}-{time.localtime(time.time()).tm_mon}-{time.localtime(time.time()).tm_mday}"
    return date

def show_today():
    date = get_today()
    return db_part.read_one_day(date)

def reminder():
    counter = 1
    for i in show_today():
        print(f"Reminder {counter}: {i[2]}")
        counter += 1

def reminder_on_date(date):
    counter = 1
    for i in show_on_date(date):
        print(f"Reminder {counter}: {i[2]}")
        counter += 1