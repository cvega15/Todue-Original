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

def app():

    application = QtWidgets.QApplication([])

    window = QtWidgets.QWidget()
    button = QtWidgets.QPushButton(window)
    label = QtWidgets.QLabel(window)
    vertical_box = QtWidgets.QVBoxLayout()

    vertical_box.addWidget(button)
    vertical_box.addWidget(label)

    window.setWindowTitle('Schedule app')
    window.setLayout(vertical_box)
    window.setGeometry(300, 200, 600, 600)

    button.setText('button')
    label.setText('hello world')
      
    window.show()
    application.exec_()

app()


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
