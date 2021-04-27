import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
  
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("dbs/tasks.db")
        self.cur = self.con.cursor()
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
        self.btns1 = []
        self.btns2 = []
        self.btns3 = []
        self.layouts = []
        self.done_layouts = []
        self.lines = []
        self.dates = []
        self.texts = []

        self.show()

    def save(self):
        # твой код
        pass

    def edit(self):
        # твой код
        pass
        
    def delete(self):
        # твой код
        pass
        
        
    def createTask(self):
        global row
        self.layouts.append(QGridLayout())
        self.lines.append(QLineEdit(self))
        self.dates.append(QDateEdit(self))
        self.texts.append(QTextEdit(self))
        self.btns1.append(QPushButton("Изменить", self))
        self.btns2.append(QPushButton("Удалить", self))
        self.btns3.append(QPushButton("Сохранить", self))

        self.btns1[self.row].clicked.connect(self.edit)
        self.btns2[self.row].clicked.connect(self.delete)
        self.btns3[self.row].clicked.connect(self.save)
        
        self.layouts[self.row].addWidget(self.lines[self.row], 0, 0)
        self.layouts[self.row].addWidget(self.dates[self.row], 0, 1)
        self.layouts[self.row].addWidget(self.texts[self.row], 0, 2)
        self.layouts[self.row].addWidget(self.btns1[self.row], 0, 3)
        self.layouts[self.row].addWidget(self.btns2[self.row], 0, 4)
        self.layouts[self.row].addWidget(self.btns3[self.row], 0, 5)

        self.tasks.addLayout(self.layouts[self.row], self.row, 0)
        
        self.row += 1
        
          
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    App.setStyle('Fusion')
    sys.exit(App.exec())