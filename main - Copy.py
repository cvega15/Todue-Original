import classes
import logger
import utils
from datetime import datetime
from datetime import timedelta
import random
import sys
from PyQt5.QtWidgets import (QMessageBox, QDateEdit, QTimeEdit, QDialog, QLineEdit, QFrame, QLabel, QSlider, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QGroupBox, QScrollArea, QSizePolicy)
from PyQt5.QtCore import (QTimer, Qt, QDate, QDateTime, QTime)
import os
import json

logger.start()
saved = ""
user_tasks = classes.User_tasks(saved)

print("Le task scheduling software has arrived")  # awesome ---> # YES :) ------>  #is this so ppl who view this understand its a meme? ----->      #meme
print('░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ \n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░\n▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░\n░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░')
print("Oh boy i worked really hard on this, i can't wait to see it run without any bugs! :D")  # !!!!VERY IMPORTANT!!!!: I added a doge meme          <------    XDDDDDDDDDDDDDDDDDDDDDDD
print("UwU, i'm a pwogwammewr, pwease give me sheckles to suppowt my famiwy of 14 childwen :3")

class App(QWidget):

    #initialize all of the variables and call gui functions
    def __init__(self):

        super(App, self).__init__()
        self.setWindowTitle('to due')
        self.setGeometry(300, 200, 600, 600)
        self.post_number = 0
        self.init_gui()

    #initialize the main window of the gui
    def init_gui(self):

        self.create_task_area()
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.addLayout(self.create_header())
        self.vertical_layout.addWidget(self.tasks_area)
        self.show()

    #create the header for the gui (i dont think it needs to be it's own function tbh, might change later)
    def create_header(self):

        header_layout = QHBoxLayout()
        btn_add_task = QPushButton('+')
        btn_add_task.setFixedSize(50, 50)
        btn_add_task.clicked.connect(self.task_adder)
        task_label = QLabel('Add Task')
        header_layout.addWidget(btn_add_task)
        header_layout.addWidget(task_label)
        return header_layout

    #create the task area for the gui, this will hold all of the tasks (probably doesn't need to be it's own function and can be made in the init_gui class)
    def create_task_area(self):

        #create a scroll area to hold tasks
        self.tasks_area = QScrollArea(self)
        self.tasks_area.setWidgetResizable(True)
        widget = QWidget()
        self.tasks_area.setWidget(widget)
        self.tasks_layout = QVBoxLayout(widget)
        self.tasks_layout.addStretch(1)

    #creates an input window for the user to input task information
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

    #used in the input window to create a new Task class
    def dialog_add_press(self):

        if(input_error_box(self.due_time_input, self.due_date_input, self.task_name_input)):
            task_identifier = random.randint(0, 1000)

            #add to the backend tasks list
            user_tasks.add_task(self.task_name_input.text(), str(datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime())))
            print(str(datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime())))
            logger.log('task added')

            #create a gui task
            task_to_add = Task(self.task_name_input.text(), datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()), task_identifier)
            self.tasks_layout.addWidget(task_to_add)

            print('task added')
            self.adder.reject()
    
    #used in the input window and closes it
    def dialog_cancel_press(self):
        print('cancel pressed')
        self.adder.reject()

class Task(QFrame):

    #initialze the Task class and all it's variables as well as create the gui
    def __init__(self, task_name, due_date, identifier):
        super(Task, self).__init__()
        self.due_date = due_date
        self.task_name = task_name
        self.identifier = identifier

        self.setFrameStyle(1)
        self.main_layout = QHBoxLayout()

        #create the left part of the task, this will be a horizontal layout with the name and the date
        self.name_and_date = QVBoxLayout()
        self.delete_and_edit = QHBoxLayout()
        self.delete = QPushButton('X')
        self.edit = QPushButton('/')
        self.delete.clicked.connect(self.button_click)
        self.delete.setFixedSize(25, 25)
        self.edit.clicked.connect(self.button_click_edit)
        self.edit.setFixedSize(25, 25)
        self.delete_and_edit.addWidget(self.delete)
        self.delete_and_edit.addWidget(self.edit)
        self.delete_and_edit.addStretch()

        self.name = QLabel(self.task_name)
        self.date = QLabel(str(self.due_date))
        self.name_and_date.addWidget(self.name)
        self.name_and_date.addWidget(self.date)
        self.name_and_date.addLayout(self.delete_and_edit)
        self.main_layout.addLayout(self.name_and_date)
        self.main_layout.addStretch()

        #create all the countdowns
        countdowns = QGridLayout()
        self.time_til = (self.due_date - datetime.today())

        self.le_days = QLabel('D: ')
        self.le_hours = QLabel('H: ')
        self.le_minutes = QLabel('M: ')
        self.le_seconds = QLabel('S: ')

        countdowns.addWidget(self.le_days, 0, 0)
        countdowns.addWidget(self.le_hours, 0, 1)
        countdowns.addWidget(self.le_minutes, 1, 0)
        countdowns.addWidget(self.le_seconds, 1, 1)
        self.main_layout.addLayout(countdowns)

        self.setLayout(self.main_layout)
        
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

    #constantly updates the time until in days, hours, minutes ad seconds
    def update_time(self):

        self.time_til = (self.due_date - datetime.today())

        self.le_days.setText('Days: ' + str(self.time_til.days))
        self.le_hours.setText('Hr: ' + str((self.time_til.days * 24 + self.time_til.seconds) // 3600))
        self.le_minutes.setText('Min: ' + str((self.time_til.seconds % 3600) // 60))
        self.le_seconds.setText('Sec: ' + str(self.time_til.seconds % 60))

    #delete button connect
    def button_click(self):

        sender = self.sender()
        if sender.text() == "X":
            user_tasks.delete_task(self.identifier)
            self.deleteLater()
            print('task deleted')
    
    #opens an edit window for the user to input a new task name, date or time
    def button_click_edit(self):

        #gets the date and time for editing
        self.date_edit = QDate.fromString(str(self.due_date.date()), 'yyyy-MM-dd')
        self.time_edit = QTime.fromString(str(self.due_date.time()))

        self.editor = QDialog()
        self.editor.setGeometry(50, 50, 250, 200)
        main_layout = QVBoxLayout()
        task_name = QLabel('Task Name')
        self.task_name_input = QLineEdit(self.task_name)
        due_date = QLabel('Due Date')
        self.due_date_input = QDateEdit(self.date_edit)
        self.due_date_input.setMinimumDate(QDate.currentDate())
        due_time = QLabel('Due Time')
        self.due_time_input = QTimeEdit(self.time_edit)

        main_layout.addWidget(task_name)
        main_layout.addWidget(self.task_name_input)
        main_layout.addWidget(due_date)
        main_layout.addWidget(self.due_date_input)

        main_layout.addWidget(due_time)
        main_layout.addWidget(self.due_time_input)
        main_layout.addSpacing(20)

        buttons = QHBoxLayout()
        button_ok = QPushButton("Edit")
        button_ok.clicked.connect(self.edit_press)
        button_close = QPushButton("Cancel")
        button_close.clicked.connect(self.edit_cancel_press)
        buttons.addWidget(button_ok)
        buttons.addWidget(button_close)
        main_layout.addLayout(buttons)
        self.editor.setLayout(main_layout)

        self.editor.addAction
        self.editor.setWindowTitle("Edit a Task")
        self.editor.exec_()

    #function for making changes to the Task classes data i.e name and due date
    def edit_press(self):

        #make sure inputs are valid using input_error_box method or else it will show an error message
        if(input_error_box(self.due_time_input, self.due_date_input, self.task_name_input)):

            #rename the task
            self.task_name = self.task_name_input.text()
            self.name.setText(self.task_name)

            #change the due date
            self.due_date = datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime())
            
            #edit the backend as well
            


            #close the editing box
            self.editor.reject()

    #cancels the edit window
    def edit_cancel_press(self):
        print('cancel pressed')
        self.editor.reject()

#functions for an error box which pops up when the users input date/time is less that the current date/time or the name is empty
def input_error_box(due_time_input, due_date_input, task_name_input):

        if(due_time_input.time() < QTime.currentTime() and due_date_input.date() == QDate.currentDate() or task_name_input.text() == ''):
            error = QMessageBox()
            error.setText("Error")
            if(task_name_input.text() == ''):
                error.setInformativeText("Please enter a task name")
            else:
                error.setInformativeText("please enter a future date")
            error.setWindowTitle("Error")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            print('error, please use a future date/time')
        else:
            return True

#runs the application
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
