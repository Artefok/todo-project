import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QWidget, QGridLayout, QDateTimeEdit, QLineEdit, QTextEdit, QDateEdit, QMessageBox, QApplication
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtCore import QDate
from reminders import *
from datetime import date

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.db = run()
        self.setWindowTitle("To-Do")
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(100, 50, 1920, 1080)

        self.layout = QVBoxLayout(self)
        self.prelayout = QHBoxLayout(self)

        self.row = 0
        
        #===================
        #widget part
        #-------------------
        
        self.label = QLabel('To-Do!', self)
        self.plus = QPushButton("+", self)
        self.plus.resize(700, 100)
        self.plus.clicked.connect(self.createTask)

        self.today = QPushButton("Tasks on today")
        self.today.resize(500, 30)
        self.today.clicked.connect(self.day_notifications)
        
##        self.grid.addWidget(self.plus, 0, 2, 3, 2)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.plus)
        self.layout.addWidget(self.today)
        self.all = QPushButton("All")
        self.active = QPushButton("Active")
        self.done = QPushButton("Done")
        self.all.clicked.connect(self.all_tasks)
        self.active.clicked.connect(self.active_tasks)
        self.done.clicked.connect(self.done_tasks)

        self.prelayout.addWidget(self.all)
        self.prelayout.addWidget(self.active)
        self.prelayout.addWidget(self.done)
        
        self.layout.addLayout(self.prelayout)
        
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.tasks = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)

        self.tasks.setSpacing(10)
        
        self.layout.addLayout(self.tasks)

        self.createTaskWithStuff

        #===================
        #CSS part
        #--------------------
        self.setStyleSheet('''background-color: #4f4f4f;
                              color: #b0b0b0;''')
        self.label.setStyleSheet("""font-size: 14.5pt;
                                    font-family: MS Gothic 2;
                                    """)
        self.all.setStyleSheet("""QPushButton{
                                      margin-top: 40px;
                                      margin-right: 0px;
                                      margin-left: 0px;
                                      border: 1px solid gray;
                                  }
                                  QPushButton:hover{
                                      background-color: #474747;
                                      height: 20px;
                                  }
                                """)
        
        self.active.setStyleSheet("""QPushButton{
                                      margin-top: 40px;
                                      margin-right: 0px;
                                      margin-left: 0px;
                                      border: 1px solid gray;
                                  }
                                  QPushButton:hover{
                                      background-color: #474747;
                                  }
                                """)
        
        self.done.setStyleSheet("""QPushButton{
                                      margin-top: 40px;
                                      margin-right: 0px;
                                      margin-left: 0px;
                                      border: 1px solid gray;
                                  }
                                  QPushButton:hover{
                                      background-color: #474747;
                                  }
                                """)
        
        
        #====================

        self.layouts = {}
        self.layouts1 = {}
        self.layouts2 = {}
        self.layouts3 = {}
        self.layouts4 = {}
        self.done_layouts = {}
        self.str_louts = {}
        self.x_pos = 0
        self.y_pos = 0

        for task in self.db.read_all():
            if task[1] != 'notnamed':
                self.createTaskWithStuff(id=task[0], name=task[1], date_exec=task[2], text=task[3], date_until=task[4], status=task[5])
            else:
                self.db.delete_the_task(task[0])

        self.show()

    def task_access(self, enable, disable):
        for i in enable:
            self.layouts[self.item][i].setReadOnly(True)
        for j in disable:
            self.layouts[self.item][i].setReadOnly(False)

    def save(self):
        self.widget = self.sender()

        self.key_list = list(self.layouts2.keys()) 
        self.val_list = list(self.layouts2.values())

        self.position = self.val_list.index(self.widget)
        self.item = self.key_list[self.position]

        self.cur_id = int(self.layouts[self.item][0].text())
        self.date = self.layouts[self.item][2].date().toString('yyyy-MM-dd')
        self.text = str(self.layouts[self.item][4].toPlainText())
        self.date1 = self.layouts[self.item][3].date().toString('yyyy-MM-dd')
        self.name = str(self.layouts[self.item][1].text())

        self.db.update(self.date, self.text, self.date1, self.cur_id, self.name  if self.name else None)

        self.layouts[self.item][1].setReadOnly(True)
        self.layouts[self.item][2].setReadOnly(True)
        self.layouts[self.item][3].setReadOnly(True)
        self.layouts[self.item][4].setReadOnly(True)
        self.layouts[self.item][5].setEnabled(True)
        self.layouts[self.item][6].setEnabled(False)
        self.layouts[self.item][7].setEnabled(True)

    def edit(self):
        self.widget = self.sender()
        self.key_list = list(self.layouts3.keys())
        self.val_list = list(self.layouts3.values())
        self.position = self.val_list.index(self.widget)
        self.item = self.key_list[self.position]
        
        self.layouts[self.item][1].setReadOnly(False)
        self.layouts[self.item][2].setReadOnly(False)
        self.layouts[self.item][3].setReadOnly(False)
        self.layouts[self.item][4].setReadOnly(False)
        self.layouts[self.item][6].setEnabled(True)
        self.layouts[self.item][7].setEnabled(False)
        
    def delete(self):
        self.widget = self.sender()
        self.key_list = list(self.layouts1.keys())
        self.val_list = list(self.layouts1.values())
        self.position = self.val_list.index(self.widget)
        self.item = self.key_list[self.position]
        self.db.delete_the_task(int(self.layouts[self.item][0].text()))

        for i in self.layouts[self.item]:
            i.deleteLater()
            if self.layouts[self.item] == None:
                break
        del self.layouts[self.item]
        
        self.y_pos -= 1

        
    # создание и отображение новой задачи    
    def createTask(self):
        self.y_pos = self.y_pos + 1
        self.elem = []

        self.task = QGridLayout()
        self.label = QLabel(f"{self.y_pos}")
        self.line = QLineEdit()
        self.line.setStyleSheet("background: #474747;")

        self.date = QDateTimeEdit()
        self.date.setDisplayFormat("yyyy-MM-dd")
        self.date.setDate(date.today())

        self.date1 = QDateTimeEdit()
        self.date1.setDisplayFormat("yyyy-MM-dd")
        self.date1.setDate(date.today())

        self.text = QTextEdit()
        self.text.setStyleSheet("background: #474747;")

        # кнопки редактирования задачи
        self.btnDelete = QPushButton(f"Delete") 
        self.btnSave = QPushButton(f"Save")
        self.btnEdit = QPushButton(f"Edit")
        self.btnDone = QPushButton(f"Done")

        task_line = [self.label, self.line, self.date, self.date1, self.text, self.btnDelete, self.btnSave, self.btnEdit, self.btnDone] # все элементы задачи

        for i in range(len(task_line)):
            self.elem.append(task_line[i])
            self.task.addWidget(task_line[i], self.y_pos, i)

        self.btnDelete.clicked.connect(self.delete) # функции, прикрепляемые к кнопкам редактирования задач
        self.btnEdit.clicked.connect(self.edit)
        self.btnSave.clicked.connect(self.save)
        self.btnDone.clicked.connect(self.doneTask)
        
        self.layouts[self.task] = self.elem # заполнение layout-ов нужными элементами
        self.layouts1[self.task] = task_line[5]
        self.layouts2[self.task] = task_line[6]
        self.layouts3[self.task] = task_line[7]
        self.layouts4[self.task] = task_line[8]
        self.str_louts[str(self.task)] = self.task

        self.btnEdit.setEnabled(False) # доп. настройки для задачи
        self.tasks.addLayout(self.task, self.y_pos, 0) # визуальный показ layout-а

        self.db.create_a_task(None, None, None, "Active", self.task, None, self.y_pos) # создание записи в БД

    # Смена статуса задачи на "Done" (сделано)
    def doneTask(self): 
        self.widget = self.sender()
        self.widget.setEnabled(False)
        self.key_list = list(self.layouts4.keys())
        self.val_list = list(self.layouts4.values())
        self.position = self.val_list.index(self.widget)
        self.item = self.key_list[self.position]
        self.db.done(int(self.layouts[self.item][0].text()))
        
    # отображение ранее созданной задачи из БД
    def createTaskWithStuff(self, id, name, date_exec, date_until, text, status):
        self.y_pos += 1
        self.elem = []

        self.task = QGridLayout()
        self.label = QLabel(f"{id}")

        self.line = QLineEdit()
        self.line.setText(name)
        self.line.setReadOnly(True)
        self.line.setStyleSheet("background: #474747;")

        self.date = QDateEdit()
        self.date.setDate(QDate.fromString(date_exec, "yyyy-MM-dd"))
        self.date.setDisplayFormat("yyyy-MM-dd")
        self.date.setReadOnly(True)

        self.date1 = QDateEdit()
        self.date1.setDate(QDate.fromString(date_until, "yyyy-MM-dd"))
        self.date1.setDisplayFormat("yyyy-MM-dd")
        self.date1.setReadOnly(True)

        self.text = QTextEdit()
        self.text.setText(text)
        self.text.setReadOnly(True)
        self.text.setStyleSheet("background: #474747;")

        self.btnDelete = QPushButton(f"Delete")
        self.btnSave = QPushButton(f"Save")
        self.btnEdit = QPushButton(f"Edit")
        self.btnDone = QPushButton(f"Done")

        self.btnSave.setEnabled(False)

        if status == "Done":
            self.btnDone.setEnabled(False)

        task_line = [self.label, self.line, self.date, self.date1, self.text, self.btnDelete, self.btnSave, self.btnEdit, self.btnDone] # все элементы задачи

        for i in range(len(task_line)):
            self.elem.append(task_line[i])
            self.task.addWidget(task_line[i], self.y_pos, i)

        self.btnDelete.clicked.connect(self.delete) # функции, прикрепляемые к кнопкам редактирования задач
        self.btnEdit.clicked.connect(self.edit)
        self.btnSave.clicked.connect(self.save)
        self.btnDone.clicked.connect(self.doneTask)
        
        self.layouts[self.task] = self.elem # заполнение layout-ов нужными элементами
        self.layouts1[self.task] = task_line[5]
        self.layouts2[self.task] = task_line[6]
        self.layouts3[self.task] = task_line[7]
        self.layouts4[self.task] = task_line[8]
        self.str_louts[str(self.task)] = self.task

        self.db.grid(int(self.layouts[self.task][0].text()), str(self.task))

        self.tasks.addLayout(self.task, id, 0)


    # СОРТИРОВКА
    
    # Отображение всех задач
    def all_tasks(self):
        self.y_pos = 0
        for task in self.db.read_all():
            self.createTaskWithStuff(id=task[0], name=task[1], date_exec=task[2], text=task[3], date_until=task[4], status=task[5])
    
    # Отображение активных задач
    def active_tasks(self):
        for task in self.db.read_all():
            if task[5] == "Active":
                self.createTaskWithStuff(id=task[0], name=task[1], date_exec=task[2], text=task[3], date_until=task[4], status=task[5])
            else:
                for i in self.layouts:
                    for p in self.layouts[i]:
                        p.deleteLater()
                    del self.layouts[i][0]
                    self.y_pos -= 1
                    
    
    # Отображение сделанных задач
    def done_tasks(self):
        for task in self.db.read_all():
            if task[5] == "Done":
                self.createTaskWithStuff(id=task[0], name=task[1], date_exec=task[2], text=task[3], date_until=task[4], status=task[5])
            else:
                for i in self.layouts[self.str_louts[task[6]]]:
                    i.deleteLater()
                del self.layouts[self.str_louts[task[6]]]
                self.y_pos -= 1

    # Отображение задач на сегодня
    def day_notifications(self):
        self.str_of_tasks = "Сегодня тебе нужно сделать данные задачи - "
        self.tasks_num = 0
        for task in self.db.read_all():
            if task[4] == str(date.today()) or task[2] == str(date.today()):
                self.str_of_tasks = self.str_of_tasks + str(task[1]) + ", "
                self.tasks_num += 1
        if self.tasks_num == 0:
            self.str_of_tasks = "На сегодня ничего не было запланировано"
        elif self.tasks_num > 0:
            self.str_of_tasks = self.str_of_tasks[:-2]
            self.str_of_tasks = self.str_of_tasks + "."
            
        QMessageBox.about(self, 'Tasks', self.str_of_tasks)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    id = QFontDatabase.addApplicationFont("C:\\Users\\Artefok\\Desktop\\OpenSans-Regular.ttf")
        # Если id равен -1, то шрифт не установлен
    if id == -1:
        print('Шрифт somefont не установлен')   
    window = Window()
    App.setStyle('Fusion')
    sys.exit(App.exec())
