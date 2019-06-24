import classes
import logger
import sys
import os
from datetime import datetime
from datetime import timedelta
from PyQt5.QtWidgets import (QMessageBox, QComboBox, QGraphicsScene, QGraphicsView, QDateEdit, QTimeEdit, QDialog, QLineEdit, QFrame, QLabel, QSlider, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QGroupBox, QScrollArea, QSizePolicy)
from PyQt5.QtCore import (QTimer, Qt, QDate, QDateTime, QTime)
import uuid

logger.start()
user_tasks = classes.User_tasks()

print("Le task scheduling software has arrived")  # awesome ---> # YES :) ------>  #is this so ppl who view this understand its a meme? ----->      #meme
print("Oh boy i worked really hard on this, i can't wait to see it run without any bugs! :D")  # !!!!VERY IMPORTANT!!!!: I added a doge meme          <------    XDDDDDDDDDDDDDDDDDDDDDDD
print("UwU, i'm a pwogwammewr, pwease give me sheckles to suppowt my famiwy of 14 childwen :3")

class App(QWidget):

    #initialize all of the variables and call gui functions
    def __init__(self):

        super(App, self).__init__()

        self.setStyleSheet(
            '''





            '''
        )

        self.setWindowTitle('to due')
        self.setGeometry(300, 200, 600, 600)
        self.create_task_area()
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.addLayout(self.create_header())
        self.vertical_layout.addWidget(self.tasks_area)
        self.show()

        self.refresh_tasks()

        timer = QTimer(self)
        timer.timeout.connect(self.countdown_update)
        timer.start(100)

    #create the header for the gui (i dont think it needs to be it's own function tbh, might change later)
    def create_header(self):

        header_layout = QHBoxLayout()
        btn_add_task = QPushButton('+')
        btn_add_task.setFixedSize(40, 40)
        btn_add_task.clicked.connect(self.task_adder)
        task_label = QLabel('Add Task')
        header_layout.addWidget(btn_add_task)
        header_layout.addWidget(task_label)

        sort_by_label = QLabel('Sort By')

        sort_by = QComboBox()
        sort_by.addItems(["Date Created", "Closest Due Date", "Time left"])
        #sort_by.currentIndexChanged.connect()
        header_layout.addStretch()
        header_layout.addWidget(sort_by_label)
        header_layout.addWidget(sort_by)

        return header_layout

    #create the task area for the gui, this will hold all of the tasks (probably doesn't need to be it's own function and can be made in the init_gui class)
    def create_task_area(self):

        #create a scroll area to hold tasks
        self.tasks_area = QScrollArea(self)
        self.tasks_area.setWidgetResizable(True)
        widget = QWidget()
        self.tasks_area.setWidget(widget)
        self.tasks_layout = QVBoxLayout(widget)
        self.tasks_layout.setAlignment(Qt.AlignTop)
        logger.log("Draw GUI")

    #goes through the entire user_tasks list and creates gui tasks based of those
    def refresh_tasks(self):
    
        for task_num in range(self.tasks_layout.count()):
            self.tasks_layout.itemAt(task_num).widget().deleteLater()

        for task in user_tasks.tasks_list:
            self.tasks_layout.addWidget(Task(task.task_name, task.time_due, task.time_made, task.id_number))

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
            

            #add to the backend tasks list
            #user_tasks.add_task(self.task_name_input.text(), datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()), datetime.today(), int(uuid.uuid1()))
            
            
            # correct ver
            user_tasks.add_task(self.task_name_input.text(), datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()), datetime.today(), str(uuid.uuid4()))
            
            #broken cus def value doesnt work
            # user_tasks.add_task(self.task_name_input.text(), datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()))
            

            logger.log('Task Added')
            self.adder.reject()
            self.refresh_tasks()
    
    #used in the input window and closes it
    def dialog_cancel_press(self):
        print('cancel pressed')
        self.adder.reject()

    #updates all of the tasks timers at the same time
    def countdown_update(self):
        for task in range(self.tasks_layout.count()):
            self.tasks_layout.itemAt(task).widget().update_time()


class Task(QFrame):

    #initialze the Task class and all it's variables as well as create the gui
    def __init__(self, task_name, due_date, time_made, identifier):
        super(Task, self).__init__()
        self.setFrameStyle(1)
        
        self.due_date = due_date
        self.task_name = task_name
        self.identifier = identifier
        self.time_made = time_made

        self.creation_due_difference = (self.due_date - self.time_made).seconds

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
        self.date = QLabel(self.due_date.strftime("Due: %m/%d/%Y Time: %I:%M %p"))
        self.name_and_date.addWidget(self.name)
        self.name_and_date.addWidget(self.date)
        self.name_and_date.addLayout(self.delete_and_edit)
        self.main_layout.addLayout(self.name_and_date)
        self.main_layout.addStretch()

        #create all the countdowns
        countdowns = QGridLayout()
        countdowns.setColumnMinimumWidth(0, 60)
        countdowns.setColumnMinimumWidth(1, 60)
        self.time_til = (self.due_date - datetime.today())

        self.le_days = QLabel('D: 0')
        self.le_hours = QLabel('H: 0')
        self.le_minutes = QLabel('M: 0')
        self.le_seconds = QLabel('S: 0')

        countdowns.addWidget(self.le_days, 0, 0, Qt.AlignLeft)
        countdowns.addWidget(self.le_hours, 0, 1, Qt.AlignLeft)
        countdowns.addWidget(self.le_minutes, 1, 0, Qt.AlignLeft)
        countdowns.addWidget(self.le_seconds, 1, 1, Qt.AlignLeft)
        self.update_time()

        self.main_layout.addLayout(countdowns)
        self.setFixedHeight(100)


        self.setLayout(self.main_layout)
    
    #constantly updates the time until in days, hours, minutes ad seconds
    def update_time(self):

        time_til = (self.due_date - datetime.today())

        if time_til.days > -1:
            frame_width = self.frameSize().width()


            self.setStyleSheet(""" 
            QFrame.Task
            {
                background-color: rgba(188, 20, 0, 0.2);
                background-clip: padding;
                border-right-width: """ + str(frame_width - (time_til.seconds * frame_width) // self.creation_due_difference) + """px;
            }
            """)
            self.le_days.setText("D: " + str(time_til.days))
            self.le_hours.setText("H: " + str((time_til.days * 24 + time_til.seconds) // 3600))
            self.le_minutes.setText("M: " + str((time_til.seconds % 3600) // 60))
            self.le_seconds.setText("S: " + str(time_til.seconds % 60))

    #delete button connect
    def button_click(self):

        sender = self.sender()
        if sender.text() == "X":
            print('frontend deleting: ' + str(self.task_name))
            user_tasks.delete_task(self.identifier)
            le_window.refresh_tasks()

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

            user_tasks.edit_task(self.identifier, self.task_name_input.text(), datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()))

            #close the editing box
            self.editor.reject()
            le_window.refresh_tasks()

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

application = QApplication(sys.argv)
le_window = App()
sys.exit(application.exec_())

