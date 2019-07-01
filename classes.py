import logger 
import os                                          
import json
import time
from threading import Timer
from datetime import datetime
from operator import itemgetter
from win10toast import ToastNotifier
import sqlite3


notifier = ToastNotifier()

#this is used for storing a list of tasks as well as adding them
class TaskCollection(object):

    # whole init needs redoing with main for the save functionality
    def __init__(self): 
        # creates task list which holds the tasks and loads the tasks if there are any
        self.tasks_list = []
        
        # new sqlite stuff -------------------------------------
        self.conn = sqlite3.connect('user_data.db')
        self.curs = self.conn.cursor()

        with self.conn:
            self.curs.execute('CREATE TABLE IF NOT EXISTS tasks(id_number INTIGER, task_name TEXT, time_due TEXT, time_made TEXT)')
        # ------------------------------------------------------

        self.load()

        logger.log("User_Tasks Created")

    def find_task(self, task_id):
        '''
        searches task list to find task
        '''
        for task in self.tasks_list: 
            if task.id_number == task_id: 
                return task 


    def add_task(self, task_name, time_due, time_made, id_number, notifications=[], save=True):
        '''
        adds a task with parameters, uses today as default time_made parameter
        '''
        # creates a Task object with params
        self.tasks_list.append(Task(task_name, time_due, time_made, id_number, notifications))
        logger.log("Adding Task")
        
        if save:
            self.save()


    def display_tasks(self):
        '''
        displays tasks and their featues
        '''
        
        for task in self.tasks_list:
            task.display_task()

        logger.log("Displaying Tasks")

    
    def edit_task(self, task_id, name_change, date_change, notifications):
        '''
        calls the edit_name and edit_due_date functions with parameters passed in
        '''

        logger.log("Editing Task")
        task = self.find_task(task_id)
        task.edit_task(name_change, date_change, notifications)
        self.save()

    
    def delete_task(self, task_id):
        '''
        removes task from the list
        '''
        print('passed in id: ' + str(task_id) + "and deleted that task")

        task = self.find_task(task_id)
        self.tasks_list.remove(task)
        self.save()
        
        logger.log("Deleted Task")
                

    def notify_task(self, task_id, message):
        for task in self.tasks_list:
            if task.id_number == task_id:
                task.notify(message)


    def save(self):
        '''
        writes data to disk
        '''
        to_save = []

        for task in self.tasks_list:
            to_add = task.get_dict()
            # new sqlite stuff ---------------------------------------
            with self.conn:
                self.curs.execute('INSERT INTO tasks(id_number, task_name, time_due, time_made) VALUES(?, ?, ?, ?)', (to_add['task id'], to_add['task name'], to_add['due date'], to_add['date created']))
            with self.conn:
                self.curs.execute('CREATE TABLE IF NOT EXISTS [' + task.id_number + '](notification TEXT)')
            for notification in task.notifications:
                with self.conn:
                    self.curs.execute('INSERT INTO [' + task.id_number + '](notification) VALUES(?);', [notification])
            # --------------------------------------------------------

            to_save.append(task.get_dict())

        save_location = os.path.dirname(os.path.abspath(__file__))
        saver = os.path.join(save_location, "save_files.txt")


        with open(saver, "w+") as handle:
            print(json.dumps(to_save), file=handle, end="")

        logger.log("Saved Data")

    def load(self):
        '''
        checks file for save data and loads it
        '''
        save_folder = os.path.dirname(os.path.abspath(__file__))
        save_file = os.path.join(save_folder, "save_files.txt")
        with open(save_file, "r") as handle:
            text = handle.read()
            self.tasks_list = json.loads("[]" if text == "" else text)
                
        logger.log(f"Loaded {len(self.tasks_list)} tasks")

        for task in self.tasks_list:
            self.add_task(
                task['task name'],
                datetime.strptime(task['due date'], "%m-/%d-/%Y, %H:%M:%S"),
                datetime.strptime(task['date created'], "%m-/%d-/%Y, %H:%M:%S"),
                task["task id"],
                task["notifications"],
                False
            )
    
    def get_task(self, task_id):
        for task in self.tasks_list:
            if task.id_number == task_id:
                return task

    def sort_alphabet(self):
        # takes each object and sorts it by its self.name.... this is the same for the following sort functions
        self.tasks_list = sorted(self.tasks_list, key=lambda task: task.task_name)
        logger.log("Sorted Alphabetically")
        self.save()

    def sort_time_remaining_asc(self):
        self.tasks_list = sorted(self.tasks_list, key=lambda task: task.time_due, reverse=True)
        logger.log("Sorted by Time")
        self.save()

    def sort_time_remaining_desc(self):
        self.tasks_list = sorted(self.tasks_list, key=lambda task: task.time_due)
        logger.log("Sorted by Reverse Time")
        self.save()
    
    def notify_tasks(self):
        for task in self.tasks_list:
            task.notify_custom()
    
    def sort_date_added(self):
        self.tasks_list = sorted(self.tasks_list, key=lambda task: task.time_made)
        logger.log("Sorted by Add Date")
        self.save()


class Task(object):

    def __init__(self, task_name, time_due, time_made, id_number, notifications):
        self.task_name = task_name
        self.time_due = time_due
        self.time_made = time_made
        self.id_number = id_number
        self.notifications = notifications

    def notify(self, message):
        notifier.show_toast(
            self.task_name,
            message,
            icon_path=None,
            duration=5,
            threaded=True
            )
    
    def notify_custom(self):
        for notification_time in self.notifications:
            if (datetime.now()).strftime("%I:%M:%S %p") == (notification_time):
                self.notify('This is Your Daily Reminder that the Task is Due ' + str(self.time_due))

    def edit_task(self, new_task_name, new_due_date, notifications):
        self.task_name = new_task_name
        self.time_due = new_due_date
        self.notifications = notifications

    def display_task(self):
        print("task name: " + self.task_name)
        print("due date: " + str(self.time_due))
        print("date created: " + str(self.time_made))
        print("task id: " + str(self.id_number))

    def get_dict(self):
        data = {
            "task name":self.task_name,
            "due date": self.time_due.strftime("%m-/%d-/%Y, %H:%M:%S"),
            "date created": self.time_made.strftime("%m-/%d-/%Y, %H:%M:%S"),
            "task id": self.id_number,
            "notifications":self.notifications
        }
        return data
