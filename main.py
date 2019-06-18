import classes
import logger
import utils
from datetime import datetime
import sys
from PyQt5.QtWidgets import (QLineEdit, QFrame, QLabel, QSlider, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QGroupBox, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt
import os

logger.start()


print("Le task scheduling software has arrived")  # awesome ---> # YES :) ------>  #is this so ppl who view this understand its a meme? ----->      #meme

print('░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ \n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░\n▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░\n░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░')
print("Oh boy i worked really hard on this, i can't wait to see it run without any bugs! :D")  # !!!!VERY IMPORTANT!!!!: I added a doge meme          <------    XDDDDDDDDDDDDDDDDDDDDDDD


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('to due')
        self.setGeometry(300, 200, 600, 600)

        self.init_gui()

    def init_gui(self):

        #create layout and add stuff
        self.create_task_area()
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.addLayout(self.create_header())
        self.vertical_layout.addWidget(self.tasks_area)

        #show the window
        self.show()

    def button_click(self):

        sender = self.sender()
        if sender.text() == "+":
            self.add_task()
            print('task added')
        elif sender.text() == "-":

            print('task deleted')

    def create_header(self):

        #create horizontal layout
        header_layout = QHBoxLayout()

        #add task button
        btn_add_task = QPushButton('+')
        btn_add_task.setFixedSize(50, 50)
        btn_add_task.clicked.connect(self.button_click)

        #create text next to the add task button
        task_label = QLabel('Add Task')

        #add widgets to the header layout
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

        self.tasks_layout.addWidget(self.create_task())

        self.tasks_layout.addStretch(1)

    def create_task(self):

        #create the qframe for the task
        task = QFrame()
        task.setFrameStyle(1)

        #create the main layour for the qframe
        main_layout = QHBoxLayout()

        #set the task's layout to the main layout
        task.setLayout(main_layout)

        #create the left part of the task, this will be a horizontal layour with the name and the date
        name_and_date = QVBoxLayout()
        delete = QPushButton('-')
        delete.setFixedSize(25, 25)
        delete.clicked.connect(self.button_click)
        name = QLabel('task name')
        date = QLabel('task due date')
        name_and_date.addWidget(name)
        name_and_date.addWidget(date)
        name_and_date.addWidget(delete)
        main_layout.addLayout(name_and_date)

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
        main_layout.addLayout(countdowns)

        return task

    def add_task(self):
        to_add = self.create_task()
        self.tasks_layout.addWidget(to_add)


def run():
    application = QApplication(sys.argv)
    le_window = Window()
    sys.exit(application.exec_())


run()


def run_program(saved=""):

    user_tasks = classes.User_tasks(saved)

    while True:
        print("1) add task \n2) display tasks \n3) edit task\n4) quit")
        user_input = int(input('>'))

        if user_input == 1:
            logger.log("User Create New Task")

            task_name = input('please enter in a task name: \n>')
            due_date = input('please enter a due date in the following format(yyyy-mm-dd hh:mm): \n>')

            user_tasks.add_task(task_name, utils.string_to_datetime(due_date + ":00"))
            
        elif user_input == 2:
            logger.log("User Display Task")

            user_tasks.display_tasks()

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
            user_tasks.save()
            print('quitting')
            break

    logger.log("End")


# saver check
save_location = os.path.dirname(os.path.abspath(__file__))
save_file = os.path.join(save_location, "save_files.txt")
with open(save_file, "r+") as handle:
    first = handle.read(1)
    if not first:
        no_save_file = []
        logger.log("No Save Found")
        run_program(no_save_file)
        
    else: 
        logger.log("Save Found")
        logger.log("Retrieving Files")
        run_program(first)