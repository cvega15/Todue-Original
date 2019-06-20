import classes
import logger
import utils
from datetime import datetime
import sys
from PyQt5.QtWidgets import (QMessageBox, QDateEdit, QTimeEdit, QDialog, QLineEdit, QFrame, QLabel, QSlider, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QGroupBox, QScrollArea, QSizePolicy)
from PyQt5.QtCore import (Qt, QDate, QDateTime, QTime)
import os
import json

logger.start()


print("Le task scheduling software has arrived")  # awesome ---> # YES :) ------>  #is this so ppl who view this understand its a meme? ----->      #meme
print('░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ \n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░\n▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░\n░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░')
print("Oh boy i worked really hard on this, i can't wait to see it run without any bugs! :D")  # !!!!VERY IMPORTANT!!!!: I added a doge meme          <------    XDDDDDDDDDDDDDDDDDDDDDDD

class App(QWidget):

    def __init__(self):

        super(App, self).__init__()
        saved = ""
        self.user_tasks = classes.User_tasks(saved)
        self.setWindowTitle('to due')
        self.setGeometry(300, 200, 600, 600)
        self.post_number = 0
        self.init_gui()

    def init_gui(self):

        self.create_task_area()
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.addLayout(self.create_header())
        self.vertical_layout.addWidget(self.tasks_area)
        self.show()

    def create_header(self):

        header_layout = QHBoxLayout()
        btn_add_task = QPushButton('+')
        btn_add_task.setFixedSize(50, 50)
        btn_add_task.clicked.connect(self.add_button_click)
        task_label = QLabel('Add Task')
        header_layout.addWidget(btn_add_task)
        header_layout.addWidget(task_label)
        return header_layout

    def create_task_area(self):

        #create a scroll area to hold tasks
        self.tasks_area = QScrollArea(self)
        self.tasks_area.setWidgetResizable(True)
        widget = QWidget()
        self.tasks_area.setWidget(widget)
        self.tasks_layout = QVBoxLayout(widget)
        self.tasks_layout.addStretch(1)

    def task_adder(self):

        self.adder = QDialog()
        self.adder.setGeometry(50, 50, 250, 200)
        main_layout = QVBoxLayout()
        task_name = QLabel('Task Name')
        self.task_name_input = QLineEdit()
        due_date = QLabel('Due Date')
        self.due_date_input = QDateEdit()
        self.due_date_input.setMinimumDate(QDate.currentDate())
        due_time = QLabel('Due Time')
        self.due_time_input = QTimeEdit()
        main_layout.addWidget(task_name)
        main_layout.addWidget(self.task_name_input)
        main_layout.addWidget(due_date)
        main_layout.addWidget(self.due_date_input)

        main_layout.addWidget(due_time)
        main_layout.addWidget(self.due_time_input)
        main_layout.addSpacing(20)

        buttons = QHBoxLayout()
        button_ok = QPushButton("Add")
        button_ok.clicked.connect(self.dialog_add_press)
        button_close = QPushButton("Cancel")
        button_close.clicked.connect(self.dialog_cancel_press)
        buttons.addWidget(button_ok)
        buttons.addWidget(button_close)
        main_layout.addLayout(buttons)
        self.adder.setLayout(main_layout)

        self.adder.addAction
        self.adder.setWindowTitle("Add a Task")
        self.adder.exec_()

    def dialog_add_press(self):
        if(self.due_time_input.time() < QTime.currentTime() and self.due_date_input.date() == QDate.currentDate() or self.task_name_input.text() == ''):
            error = QMessageBox()
            error.setText("Error")
            if(self.task_name_input.text() == ''):
                error.setInformativeText("Please enter a task name")
            else:
                error.setInformativeText("please enter a future date")
            error.setWindowTitle("Error")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            print('error, please use a future date/time')
        else:
            self.user_tasks.add_task(self.task_name_input.text(), str(datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime())))
            print(str(datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime())))
            logger.log('task added')

            task_to_add = Task(self.task_name_input.text(), datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()))

            self.tasks_layout.addWidget(task_to_add)
            print('task added')
            self.adder.reject()
    
    def dialog_cancel_press(self):
        print('cancel pressed')
        self.adder.reject()

    def add_button_click(self):
        self.task_adder()

class Task(QFrame):

    def __init__(self, task_name, due_date):
        super(Task, self).__init__()
        self.setFrameStyle(1)
        self.main_layout = QHBoxLayout()

        #create the left part of the task, this will be a horizontal layour with the name and the date
        name_and_date = QVBoxLayout()
        delete = QPushButton('-')
        delete.clicked.connect(self.button_click)
        delete.setFixedSize(25, 25)

        name = QLabel(task_name)
        date = QLabel(str(due_date))
        name_and_date.addWidget(name)
        name_and_date.addWidget(date)
        name_and_date.addWidget(delete)
        self.main_layout.addLayout(name_and_date)

        #create all the countdowns
        countdowns = QGridLayout()
        days = QLabel('10 D')
        hours = QLabel('20 H')
        minutes = QLabel('30 M')
        seconds = QLabel('40 S')
        countdowns.addWidget(days, 0, 0)
        countdowns.addWidget(hours, 0, 1)
        countdowns.addWidget(minutes, 1, 0)
        countdowns.addWidget(seconds, 1, 1)
        self.main_layout.addLayout(countdowns)

        self.setLayout(self.main_layout)

    def button_click(self):

        sender = self.sender()
        if sender.text() == "-":

            self.deleteLater()
            print('task deleted')

application = QApplication(sys.argv)
le_window = App()
sys.exit(application.exec_())
'''
def run_program(saved=""):

    while True:

        elif user_input == 3:
            logger.log("User editing task")
            user_tasks.display_tasks()

            to_edit = input('please enter in the name of the task that you want to edit: \n>')
            edit_selection = int(input('1) rename task \n2) change due date \n3) cancel: \n>'))

            if(edit_selection == 1):
                
                name_change = input('enter name change: \n>')
                user_tasks.edit_task(to_edit, name_change, None)

                logger.log("Name Changed")

            elif(edit_selection == 2):

                date_change = input('please enter a change date in the following format(yyyy-mm-dd hh:mm): \n>')
                user_tasks.edit_task(to_edit, None, utils.string_to_datetime(date_change + ":00"))

                logger.log("Date Changed")

            else:
                break

        else:
            user_tasks.serialize()
            user_tasks.save()
            print('quitting')
            logger.log("End")
            break
'''
# saver check
save_location = os.path.dirname(os.path.abspath(__file__))
save_file = os.path.join(save_location, "save_files.txt")
with open(save_file, "r") as handle:
    first = handle.read()
    if not first:
        logger.log("No Save Found")
        run_program("")
        
    elif first: 
        logger.log("Save Found")
        logger.log("Retrieving Files")
        print(first)
        task_dict = json.loads(first)
        run_program(task_dict)

        # error for the loads json function:
        # Traceback (most recent call last):
        # File "c:\dev\zip_code\main.py", line 79, in <module>
        #     task_dict = json.loads(first)
        # File "C:\Users\Thomas\Miniconda3\lib\json\__init__.py", line 348, in loads
        #     return _default_decoder.decode(s)
        # File "C:\Users\Thomas\Miniconda3\lib\json\decoder.py", line 337, in decode
        #     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        # File "C:\Users\Thomas\Miniconda3\lib\json\decoder.py", line 355, in raw_decode
        #     raise JSONDecodeError("Expecting value", s, err.value) from None
        # json.decoder.JSONDecodeError: Expecting value: line 1 column 2 (char 1)

    else:
        print("No") #             <- meme
        exit()
