import classes
import logger
import utils
from datetime import datetime
import sys
from PyQt5.QtWidgets import (QLineEdit, QLabel, QSlider, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QGroupBox, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt

logger.start()
# this is where we have to recall, at the beginning before anything starts
user_tasks = classes.User_tasks()

print("Le task scheduling software has arrived") #awesome ---> # YES :) ------>  #is this so ppl who view this understand its a meme? ----->      #meme
print('░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ \n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░\n▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░\n░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░')
print("Oh boy i worked really hard on this, i can't wait to see it run without any bugs! :D") #!!!!VERY IMPORTANT!!!!: I added a doge meme

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
            print('task added')

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
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        self.tasks_layout.addWidget(self.create_task())
        
        self.tasks_layout.addStretch(1)


    def create_task(self):

        #create the groupbox
        task_group = QGroupBox('task group')
    
        #create vbox 
        name_and_date = QVBoxLayout()

        #create a grid 2x2 layout for the time until feature
        countdowns = QGridLayout()

        #create and add data for the countdowns grid
        days = QLabel('10')
        hours = QLabel('20')
        minutes = QLabel('30')
        seconds = QLabel('40')
        countdowns.addWidget(days, 0, 0)
        countdowns.addWidget(days, 0, 1)
        countdowns.addWidget(days, 1, 0)
        countdowns.addWidget(days, 1, 1)

        #create and add data for the name_and_date layout
        task_name = QLabel('task name')
        date_due = QLabel('due date')
        name_and_date.addWidget(task_name)
        name_and_date.addWidget(date_due)

        #combine objects into group        
        #task_group.setLayout(name_and_date)
        #task_group.setLayout(countdowns)

        return task_group
    
def run():
    application = QApplication(sys.argv)
    le_window = Window()
    sys.exit(application.exec_())
run()

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

            logger.log("name changed")

        elif(edit_selection == 2):

            date_change = input('please enter a change date in the following format(yyyy-mm-dd hh:mm): \n>')
            user_tasks.edit_task(to_edit, None, utils.string_to_datetime(date_change + ":00"))

            logger.log("date changed")

        else:
            break

    else:
        user_tasks.save()
        print('quitting')
        break

logger.log("End")
