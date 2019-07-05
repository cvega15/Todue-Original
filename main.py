import classes
import logger
import sys
import os
from datetime import datetime
from datetime import timedelta
from PyQt5.QtWidgets import (QTabWidget, QMessageBox, QComboBox, QGraphicsScene, QGraphicsView, QDateEdit, QTimeEdit, QDialog, QLineEdit, QFrame, QLabel, QSlider, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QGroupBox, QScrollArea, QSizePolicy)
from PyQt5.QtCore import (QTimer, Qt, QDate, QDateTime, QTime)
import uuid
import time
from win10toast import ToastNotifier
from typing import List

logger.start("log.txt")
logger.save_create("save_files.txt")
user_tasks = classes.TaskCollection()
notifier = ToastNotifier()


# the main gui area
class App(QWidget):

    #initialize all of the variables and call gui functions
    def __init__(self):
        super(App, self).__init__()
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


    def create_header(self):
        # create the header for the gui (i dont think it needs to be it's own function tbh, might change later)

        header_layout = QHBoxLayout()
        btn_add_task = QPushButton('+')
        btn_add_task.setFixedSize(40, 40)
        btn_add_task.clicked.connect(lambda: TaskAddEditor('Add a task', 'Add', None))
        task_label = QLabel('Add Task')
        header_layout.addWidget(btn_add_task)
        header_layout.addWidget(task_label)

        sort_by_menu = QLabel('Sort By')

        sort_by = QComboBox()
        sort_by.addItems(["Alphabetic", "Date Created", "Furthest Due Date", "Time Left"])
        sort_by.currentIndexChanged.connect(self.sort_by_func)
        header_layout.addStretch()
        header_layout.addWidget(sort_by_menu)
        header_layout.addWidget(sort_by)

        return header_layout

    def sort_by_func(self, choice):
        # calls backend sort functions
        if choice == 0:
            print('sorting alphabetically')
            self.refresh_tasks('alpha')
        elif choice == 1:
            print('sorting by date created')
            self.refresh_tasks('da')
        elif choice == 2:
            print('sorting by furthest due date')
            self.refresh_tasks('tra')
        elif choice == 3:
            print('sorting by amount of time left')
            self.refresh_tasks('trd')

    def create_task_area(self):
        # create a scroll area to hold tasks -- # create the task area for the gui, this will hold all of the tasks (probably doesn't need to be it's own function and can be made in the init_gui class)
        self.tasks_area = QScrollArea(self)
        self.tasks_area.setWidgetResizable(True)
        widget = QWidget()
        self.tasks_area.setWidget(widget)
        self.tasks_layout = QVBoxLayout(widget)
        self.tasks_layout.setAlignment(Qt.AlignTop)
        logger.log("Drawing GUI")

    def refresh_tasks(self, sort_by='alpha'):

        # erase all current tasks in layout
        for task_num in range(self.tasks_layout.count()):
            self.tasks_layout.itemAt(task_num).widget().deleteLater()

        # get current tasks from database
        all_tasks = user_tasks.get_tasks(sort_by)
        
        #creates new task windows based off the database data
        for task_tuple in all_tasks:
            self.tasks_layout.addWidget(TaskWindow(task_tuple[0], task_tuple[1], task_tuple[2], task_tuple[3], task_tuple[4]))

    def countdown_update(self):
    # updates all of the tasks timers at the same time
        for task in range(self.tasks_layout.count()):
            try:
                self.tasks_layout.itemAt(task).widget().update_time()
            except:
                pass


# singular task item
class TaskWindow(QFrame):

    #initialze the TaskWindow class and all it's variables as well as create the gui
    def __init__(self, identifier, task_name, due_date, time_made, notifications: List[datetime]) -> None:
        super(TaskWindow, self).__init__()
        self.setFrameStyle(1)

        self.due_date = due_date
        self.task_name = task_name
        self.identifier = identifier
        self.time_made = time_made
        self.notifications = notifications

        self.creation_due_difference = (self.due_date - self.time_made).total_seconds()

        self.main_layout = QHBoxLayout()

        #create the left part of the task, this will be a horizontal layout with the name and the date
        self.name_and_date = QVBoxLayout()
        self.delete_and_edit = QHBoxLayout()
        self.delete = QPushButton('X')
        self.edit = QPushButton('/')
        self.delete.clicked.connect(self.button_click)
        self.delete.setFixedSize(25, 25)
        self.edit.clicked.connect(lambda: TaskAddEditor('Edit Task', 'Edit', self.identifier))
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
        self.time_until = (self.due_date - datetime.today())

        self.days = QLabel('D: 0')
        self.hours = QLabel('H: 0')
        self.minutes = QLabel('M: 0')
        self.seconds = QLabel('S: 0')

        countdowns.addWidget(self.days, 0, 0, Qt.AlignLeft)
        countdowns.addWidget(self.hours, 0, 1, Qt.AlignLeft)
        countdowns.addWidget(self.minutes, 1, 0, Qt.AlignLeft)
        countdowns.addWidget(self.seconds, 1, 1, Qt.AlignLeft)
        self.update_time()

        self.main_layout.addLayout(countdowns)
        self.setFixedHeight(100)

        self.setLayout(self.main_layout)

 
    # constantly updates the time until in days, hours, minutes and secons
    def update_time(self):
      
        time_until = (self.due_date - datetime.today())
        frame_width = self.frameSize().width()

        if time_until.days > -1:

            if(time_until.seconds == 1):
                self.notify()
            elif(time_until.total_seconds == 600):
                self.notify()
            elif(time_until.total_seconds == 3600):
                self.notify()
            elif(time_until.total_seconds == 86400):
                self.notify()

            if((time_until.seconds % 60) == 59):
                print('ok testing')
                for notification in self.notifications:
                    print('e: ' + str(notification.strftime('%H:%M')))
                    print('now: ' + str(datetime.now().strftime('%H:%M')))
                    if notification.strftime('%H:%M') == datetime.now().strftime('%H:%M'):
                        print('notifeying') 
                        self.notify()

            # draws the countdown bar on the task window
            self.setStyleSheet(f"""  
                QFrame.TaskWindow
                {{
                background-color: rgba(70, 130, 180, 0.2);
                background-clip: padding;
                border-right-width: {str(frame_width - (time_until.total_seconds() * frame_width) // self.creation_due_difference)} px;
                }}
                """)
            self.days.setText("D: " + str(time_until.days))
            self.hours.setText("H: " + str((time_until.days * 24 + time_until.seconds) // 3600))
            self.minutes.setText("M: " + str((time_until.seconds % 3600) // 60))
            self.seconds.setText("S: " + str(time_until.seconds % 60))
        else:
            self.setStyleSheet('QFrame.TaskWindow {background-color: transparent;}')

    #goes through each task and sends notifications
    def notify(self):

        self.simple_notification('task_name', 'yo, remember that this task is due like very soon man')

    # sends a notification to windows
    def simple_notification(self, header, info):
        
        notifier.show_toast(
            header,
            info,
            icon_path=None,
            duration=5,
            threaded=True
            )

    # deletes the task
    def button_click(self):
        
        sender = self.sender()
        if sender.text() == "X":
            user_tasks.delete_task(self.identifier)
            gui_window.refresh_tasks()


# the window that pops up and asks for information about a task
class TaskAddEditor(QDialog):

    #initialize everything
    def __init__(self, dialog_name, button_name, identifier = None):
        super(TaskAddEditor, self).__init__()
        self.dialog_name = dialog_name
        self.button_name = button_name
        self.identifier = identifier

        self.setGeometry(50, 50, 300, 250)

        self.tabs = QTabWidget()
        self.tabs.tab_1 = QWidget()
        self.tabs.tab_2 = QWidget()
        
        self.tabs.addTab(self.tabs.tab_1, "Basic Info")
        self.tabs.addTab(self.tabs.tab_2, "Notifications")

        self.tab_1()
        self.tab_2()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)

        buttons = QHBoxLayout()

        button_ok = QPushButton(self.button_name)
        button_close = QPushButton("Cancel")
        button_ok.clicked.connect(self.dialog_button_click)
        button_close.clicked.connect(self.dialog_cancel_click)
        buttons.addWidget(button_ok)
        buttons.addWidget(button_close)

        main_layout.addLayout(buttons)

        self.setLayout(main_layout)

        self.setWindowTitle(dialog_name)
        self.exec_()


    def tab_1(self):
        # main layout
        layout = QVBoxLayout()

        task_name = QLabel('Task Name')
        due_date = QLabel('Due Date')
        due_time = QLabel('Due Time')

        if(self.button_name == "Add"):
            self.task_name_input = QLineEdit()
            self.due_date_input = QDateEdit()
            self.due_date_input.setMinimumDate(QDate.currentDate())
            self.due_time_input = QTimeEdit()

        else:

            task_info = user_tasks.get_task(self.identifier)

            self.task_name_input = QLineEdit(task_info[1])
            self.due_date_input = QDateEdit(task_info[2].date())
            self.due_date_input.setMinimumDate(QDate.currentDate())
            self.due_time_input = QTimeEdit(task_info[2].time())

        layout.addWidget(task_name)
        layout.addWidget(self.task_name_input)
        layout.addWidget(due_date)
        layout.addWidget(self.due_date_input)
        layout.addWidget(due_time)
        layout.addWidget(self.due_time_input)
        layout.addSpacing(20)

        self.tabs.tab_1.setLayout(layout)

    def tab_2(self):
        layout = QVBoxLayout()

        page_name = QLabel('Notification Settings')
        layout.addWidget(page_name)

        add_notification_area = QHBoxLayout()

        description = QLabel('Remind Me Everyday At: ')
        self.time_input = QTimeEdit()
        add_notification = QPushButton('+')
        add_notification.setFixedSize(30, 30)
        add_notification.clicked.connect(self.add_notification)

        add_notification_area.addWidget(description)
        add_notification_area.addWidget(self.time_input)
        add_notification_area.addWidget(add_notification)
    
        layout.addLayout(add_notification_area)

        your_notifications = QLabel('Your Notifications:')

        layout.addWidget(your_notifications)

        #create a scroll area to hold notifications
        notifications_area = QScrollArea(self)
        notifications_area.setWidgetResizable(True)
        widget = QWidget()
        notifications_area.setWidget(widget)
        self.notifications_layout = QVBoxLayout(widget)
        notifications_area.setAlignment(Qt.AlignTop)
        self.notifications_layout.setAlignment(Qt.AlignTop)
        
        layout.addWidget(notifications_area)

        if self.identifier is not None:

            #get a list of datetime objects
            notifications = user_tasks.get_notifications(self.identifier)

            #add notifications to the tab
            for notification_date in notifications:
                self.notifications_layout.addWidget(Notification(notification_date))

        self.tabs.tab_2.setLayout(layout)

    def add_notification(self):
        # adds a notification to the layout of notifications
        for index in range(self.notifications_layout.count()):
            if ((self.notifications_layout.itemAt(index).widget().notification_time) > (self.time_input.time().toPyTime())):
                self.notifications_layout.insertWidget(index, Notification(self.time_input.time().toPyTime()))
                return 
            elif (self.notifications_layout.itemAt(index).widget().notification_time) == self.time_input.time().toPyTime():
                error = QMessageBox()
                error.setText("Time Already Set")
                error.exec_()
                return 
            
        self.notifications_layout.addWidget(Notification(self.time_input.time().toPyTime()))

    def dialog_button_click(self):
        # when add is pressed
        if(input_error_box(self.due_time_input, self.due_date_input, self.task_name_input)):

            notification_dates = []
            for notification in range(self.notifications_layout.count()):
                notification_dates.append(self.notifications_layout.itemAt(notification).widget().notification_time)
            
            if(self.button_name == 'Add'):
                print(notification_dates)
                user_tasks.add_task(
                    self.task_name_input.text(), 
                    datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()), 
                    datetime.today(), 
                    str(uuid.uuid4()), 
                    notification_dates)
            else:
                print(notification_dates) 
                user_tasks.edit_task(
                    self.identifier,
                    self.task_name_input.text(), 
                    datetime.combine(self.due_date_input.date().toPyDate(), self.due_time_input.time().toPyTime()),
                    notification_dates)

            self.reject()
            gui_window.refresh_tasks()

    def dialog_cancel_click(self):
        #used in the input window and closes it
        self.reject()


# notification widget
class Notification(QFrame):

    def __init__(self, notification_time: datetime.time) -> None:

        super(Notification, self).__init__()
        self.setFrameStyle(1)
        self.notification_time = notification_time
        main_layout = QHBoxLayout()
        display_time = QLabel(self.notification_time.strftime('%I:%M %p'))
        delete_button = QPushButton('-')
        delete_button.setFixedSize(32, 22)
        delete_button.clicked.connect(lambda: self.deleteLater())
        main_layout.addWidget(display_time)
        main_layout.addWidget(delete_button)
        self.setFixedHeight(45)
        self.setLayout(main_layout)


def input_error_box(due_time_input, due_date_input, task_name_input):
    # functions for an error box which pops up when the users input date/time is less that the current date/time or the name is empty
    if(due_time_input.time() < QTime.currentTime() and due_date_input.date() == QDate.currentDate() or task_name_input.text() == ''):
        error = QMessageBox()
        error.setText("Error")
        if(task_name_input.text() == ''):
            error.setInformativeText("Please Enter a Task Name")
        else:
            error.setInformativeText("Please Enter a Date in the Future")
            error.setWindowTitle("Error")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    else:
        return True


application = QApplication(sys.argv)
gui_window = App()
sys.exit(application.exec_())

