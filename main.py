import classes
import logger
import utils
from datetime import datetime
import sys
from PyQt5 import QtWidgets

logger.start()
# this is where we have to recall, at the beginning before anything starts
user_tasks = classes.User_tasks()

print("hello, le task scheduling program has arrived! this'll be ebic") #awesome ---> # YES :) ------>  #is this so ppl who view this understand its a meme? ----->      #meme

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_gui()
    
    def init_gui(self):
        self.button = QtWidgets.QPushButton('test button')
        self.label = QtWidgets.QLabel('I have not been clicked yet')

        horizontal_box = QtWidgets.QHBoxLayout()
        horizontal_box.addStretch()
        horizontal_box.addWidget(self.label)
        horizontal_box.addStretch()

        vertical_box = QtWidgets.QVBoxLayout()
        vertical_box.addWidget(self.button)
        vertical_box.addLayout(horizontal_box)

        self.setWindowTitle('to due')
        self.setGeometry(300, 200, 600, 600)
        self.show()
        self.setLayout(vertical_box)

application = QtWidgets.QApplication(sys.argv)
le_window = Window()
sys.exit(application.exec_())


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
