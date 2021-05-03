from reminders import run
from os import getcwd
con = run(f"{getcwd()}\\dbs\\tasks.db")
while True:
    act = input("Какой вид работы с напоминаниями будет?\n1)Создание\n2)Чтение\n3)Удаление\n4)Изменение\n5)Выход\n")
    #clear
    if "$" in act:
        act = act[1:]
        if act == "clear":
            con.clear()
        else:
            print(f"ConsoleError: unknown command: '${act}'")
    #create a task  
    elif act == "1":
        date = input("На какой день будет это напоминание?(желательно использовать формат ГГГГ-М-Д)\n")
        date_until = input("До какого дня будет это напоминание?(желательно использовать формат ГГГГ-М-Д)\n")
        name = input("Название напоминания(не обязательно)\n")
        text = input("Текст напоминания\n")
        time = input("Время напоминания\n")
        con.create_a_task(date, text, date_until, time, name)
    #show
    elif act == "2":
        act = input("Показать когда? Сегодня/На дату/Всё(С/НД/В)\n")
        #today
        if act.upper() == "С":
            con.reminder()
        #on day
        elif act.upper() == "НД":
            date = input("На какой день показать напоминание?(желательно использовать формат ГГГГ-М-Д)\n")
            con.reminder_on_date(date)
        #all
        elif act.upper() == "В":
            con.reminder_all()
        else:
            print("Ответ не корректен")
    #delete by id
    elif act == "3":
        task_id = input("Идентификатор напоминания\n")
        con.delete_the_task(task_id)
    #update by id
    elif act == "4":
        task_id = input("Идентификатор напоминания\n")
        date = input("На какой день будет это напоминание?(желательно использовать формат ГГГГ-М-Д)\n")
        date_until = input("До какого дня будет это напоминание?(желательно использовать формат ГГГГ-М-Д)\n")
        name = input("Название напоминания(не обязательно)\n")
        text = input("Текст напоминания\n")
        text = input("Время напоминания\n")
        con.update(date_until, text, task_id, name)
    #exit
    elif act == "5":
        con.con_exit()
        break
    else:
        print("Ответ не корректен")