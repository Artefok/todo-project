import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from reminders import *
  
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.db = run()
        self.setWindowTitle("To-Do")
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(100, 50, 1920, 1080)

        self.layout = QVBoxLayout(self)
        self.prelayout = QHBoxLayout(self)

        self.grid = QGridLayout(self)

        self.row = 0
        #===================
        #widget part
        #-------------------
        
        self.label = QLabel('To-Do!', self)
        
        self.plus = QPushButton("+", self)
        self.plus.resize(700, 30)
        self.plus.clicked.connect(self.createTask)
        
##        self.grid.addWidget(self.plus, 0, 2, 3, 2)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.plus)
        self.all = QPushButton("Все")
        self.active = QPushButton("Активные")
        self.done = QPushButton("Сделанные")

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

        #===================
        #CSS part
        #--------------------
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
                                      background-color: lightgray;
                                  }
                                """)
        
        self.active.setStyleSheet("""QPushButton{
                                      margin-top: 40px;
                                      margin-right: 0px;
                                      margin-left: 0px;
                                      border: 1px solid gray;
                                  }
                                  QPushButton:hover{
                                      background-color: lightgray;
                                  }
                                  QPushButton:pressed{
                                      box-shadow: 5px 10px 8px;
                                  }
                                """)
        
        self.done.setStyleSheet("""QPushButton{
                                      margin-top: 40px;
                                      margin-right: 0px;
                                      margin-left: 0px;
                                      border: 1px solid gray;
                                  }
                                  QPushButton:hover{
                                      background-color: lightgray;
                                  }
                                """)
        
        
        #====================

        self.layouts = {}
        self.layouts1 = {}
        self.layouts2 = {}
        self.layouts3 = {}
        self.x_pos = 0
        self.y_pos = 0

        self.show()

    def save(self):
        self.widget = self.sender()
        self.key_list = list(self.layouts2.keys())
        self.val_list = list(self.layouts2.values())
        self.position = self.val_list.index(self.widget)
        self.item = self.key_list[self.position]
        self.db.create_a_task()
        
        self.layouts[self.item][1].setReadOnly(True)
        self.layouts[self.item][2].setReadOnly(True)
        self.layouts[self.item][3].setReadOnly(True)

    def edit(self):
        self.widget = self.sender()
        self.key_list = list(self.layouts3.keys())
        self.val_list = list(self.layouts3.values())
        self.position = self.val_list.index(self.widget)
        self.item = self.key_list[self.position]
        
        self.layouts[self.item][1].setReadOnly(False)
        self.layouts[self.item][2].setReadOnly(False)
        self.layouts[self.item][3].setReadOnly(False)
        
    def delete(self):
        self.widget = self.sender()
        self.key_list = list(self.layouts1.keys())
        self.val_list = list(self.layouts1.values())
        self.position = self.val_list.index(self.widget)
        self.item = self.key_list[self.position]

        for i in self.layouts[self.item]:
            i.deleteLater()
            if self.layouts[self.task] == None:
                break
        
        self.y_pos -= 1

        
        
    def createTask(self):
        self.y_pos = self.y_pos + 1

        self.elem = []

        self.task = QGridLayout()
        self.label = QLabel(f"{self.y_pos}")
        self.line = QLineEdit()
        self.date = QDateEdit()
        self.text = QTextEdit()
        self.button = QPushButton(f"Delete")
        self.button1 = QPushButton(f"Save")
        self.button2 = QPushButton(f"Edit")

        self.elem.append(self.label)
        self.elem.append(self.line)
        self.elem.append(self.date)
        self.elem.append(self.text)
        self.elem.append(self.button)
        self.elem.append(self.button1)
        self.elem.append(self.button2)

        self.task.addWidget(self.label, self.y_pos, 0)
        self.task.addWidget(self.line, self.y_pos, 1)
        self.task.addWidget(self.date, self.y_pos, 2)
        self.task.addWidget(self.text, self.y_pos, 3)
        self.task.addWidget(self.button2, self.y_pos, 4)
        self.task.addWidget(self.button1, self.y_pos, 5)
        self.task.addWidget(self.button, self.y_pos, 6)

        self.button.clicked.connect(self.delete)
        self.button2.clicked.connect(self.edit)
        self.button1.clicked.connect(self.save)
        
        self.layouts[self.task] = self.elem
        self.layouts1[self.task] = self.button
        self.layouts2[self.task] = self.button1
        self.layouts3[self.task] = self.button2

        self.tasks.addLayout(self.task, self.y_pos, 0)
        
        
          
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    App.setStyle('Fusion')
    sys.exit(App.exec())



