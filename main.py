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
        self.setGeometry(0, 0, 1520, 800)

        self.layout = QHBoxLayout(self)

        
        self.grid = QGridLayout()

        self.row = 0
        #===================
        #widget part
        #-------------------
        
        self.label = QLabel('To-Do!', self)
        
        self.btn = QPushButton('Настройки', self)
        self.btn.resize(self.btn.sizeHint())
        self.plus = QPushButton("+", self)
        self.plus.resize(600, 30)
        self.plus.clicked.connect(self.createTask)
        

        self.grid.addWidget(self.label, 0, 1, 1, 2)
        self.grid.addWidget(self.btn, 0, 4, 1, 1)
        self.grid.addWidget(self.plus, 0, 2, 3, 2)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.tasks = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)

        self.tasks.setSpacing(30)
        self.tasks.setContentsMargins(30,70,30,70)

        self.grid.addLayout(self.tasks, 2, 1, 4, 4)

        #===================
        #CSS part
        #--------------------
        self.label.setStyleSheet("""font-size: 14.5pt;
                                    font-family: MS Gothic 2;
                                    """)
        self.btn.setStyleSheet("""font-size: 9pt;
                                  font-family: MS Gothic 2;""")
        
        #====================
        self.btns1 = []
        self.btns2 = []
        self.layouts = []
        self.lines = []
        self.dates = []
        self.texts = []

        self.show()
    def createTask(self):
        global row
        self.layouts.append(QGridLayout())
        self.lines.append(QLineEdit(self))
        self.dates.append(QDateEdit(self))
        self.texts.append(QTextEdit(self))
        self.btns1.append(QPushButton("Изменить", self))
        self.btns2.append(QPushButton("Удалить", self))

        self.layouts[self.row].addWidget(self.lines[self.row], 0, 0)
        self.layouts[self.row].addWidget(self.dates[self.row], 0, 1)
        self.layouts[self.row].addWidget(self.texts[self.row], 0, 2)
        self.layouts[self.row].addWidget(self.btns1[self.row], 0, 3)
        self.layouts[self.row].addWidget(self.btns2[self.row], 0, 4)

        self.tasks.addLayout(self.layouts[self.row], self.row, 0)
        
        self.row += 1
        
          
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    App.setStyle('Fusion')
    sys.exit(App.exec())



