import classes
import logger
import utils
from datetime import datetime
import sys
from PyQt5.QtWidgets import (QLineEdit, QLabel, QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt

logger.start()
# this is where we have to recall, at the beginning before anything starts
user_tasks = classes.User_tasks()

print("Le task scheduling software has arrived") #awesome ---> # YES :) ------>  #is this so ppl who view this understand its a meme? ----->      #meme
print('░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ \n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░\n▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░\n░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░')
print("WOow i've worked really hard on this, i can't wait to see it run flawlesly :D") #---> IMPORTANT, I added a doge meme

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_gui()
    
    def init_gui(self):

        vertical_layout = QVBoxLayout()
        header_layout = QHBoxLayout()

        btn_add_task = QPushButton('+')
        btn_add_task.clicked.connect(self.button_click)
        btn_add_task.setVerticalPolicy(500)

        self.add_task_label = QLabel('Add Task')
        self.tasks_area = QScrollArea()

        header_layout.addWidget(btn_add_task)
        header_layout.addWidget(self.add_task_label)
        header_layout.addStretch()

        vertical_layout.addLayout(header_layout)
        vertical_layout.addWidget(self.tasks_area)
        vertical_layout.addStretch()

        self.setLayout(vertical_layout)
        self.setWindowTitle('to due')
        self.setGeometry(300, 200, 600, 600)
        
        '''
        self.line_edit = QLineEdit()
        self.print_to_console = QPushButton('print to console')
        self.button = QPushButton('test button')
        self.label = QLabel('I have not been clicked yet')
        self.slider = QSlider(Qt.Horizontal)

        self.slider.setMinimum(1)
        self.slider.setMaximum(10)
        self.slider.setValue(5)
        self.slider.setTickInterval(2)
        self.slider.setTickPosition(QSlider.TicksBelow)

        horizontal_box = QHBoxLayout()
        horizontal_box.addStretch()
        horizontal_box.addWidget(self.label)
        horizontal_box.addStretch()

        vertical_box = QVBoxLayout()
        vertical_box.addWidget(self.button)
        vertical_box.addWidget(self.line_edit)
        vertical_box.addWidget(self.print_to_console)
        vertical_box.addLayout(horizontal_box)
        vertical_box.addWidget(self.slider)

        self.setLayout(vertical_box)
        self.setWindowTitle('to due')
        self.setGeometry(300, 200, 600, 600)

        self.button.clicked.connect(self.button_click)
        self.print_to_console.clicked.connect(self.button_click)
        '''
        self.show()
    
    def button_click(self):

        sender = self.sender()
        if sender.text() == "+":
            print('task added')
    
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
