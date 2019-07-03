import logger 
import os                                          
import json
import time
from threading import Timer
from datetime import datetime
from operator import itemgetter
from win10toast import ToastNotifier
import sqlite3
from typing import List

notifier = ToastNotifier()

#this is used for storing a list of tasks as well as adding them
class TaskCollection(object):

    # constructor
    def __init__(self):
        
        #creates a connection to the database and creates a database file
        self.conn = sqlite3.connect('user_data.db')
        self.curs = self.conn.cursor()

        #creates a table to hold tasks if one doesn't exist
        with self.conn:
            self.curs.execute("CREATE TABLE IF NOT EXISTS tasks(id_number TEXT, task_name TEXT, time_due TEXT, time_made TEXT)")
        
        logger.log("User_Tasks Created")



    # adds a task to the sqlite database 
    def add_task(self, task_name: str, time_due: datetime, time_made: datetime, id_number: str, notifications=[]) -> None:
        '''
        adds a task with parameters, uses today as default time_made parameter
        '''

        # new sqlite stuff
        with self.conn:
            self.curs.execute("INSERT INTO tasks(id_number, task_name, time_due, time_made) VALUES(?, ?, ?, ?)", (id_number, task_name, time_due.strftime('%m-%d-%Y, %H:%M:%S'), time_made.strftime('%m-%d-%Y, %H:%M:%S')))
        with self.conn:
            self.curs.execute(f"CREATE TABLE IF NOT EXISTS [{id_number}] (notification TEXT)")
         ihjjjkjkjjkhjhkillme
        for notification in notifications:
            with self.conn:
                self.curs.execute(f"INSERT INTO [{id_number}] (notification) VALUES(?);", (notification,))
        '''
        with self.conn:
            [lambda: self.curs.execute(f"INSERT INTO [{id_number}] (notification) VALUES(?);", (notification,)) for notification in notifications]
        '''

        logger.log("Adding Task")

    # edits a task in the sqlite database
    def edit_task(self, task_id: str, name_change: str, date_change: datetime, notifications=[]) -> None:
        '''
        calls the edit_name and edit_due_date functions with parameters passed in
        '''

        #edits the task row in the tasks table
        with self.conn:
            self.curs.execute(f"UPDATE tasks SET task_name='{name_change}', time_due='{date_change.strftime('%m-%d-%Y, %H:%M:%S')}' WHERE id_number='{task_id}';")

        #edits the task's notification's table
        with self.conn:
            self.curs.execute(f"DROP TABLE [{task_id}]")
        with self.conn:
            self.curs.execute(f"CREATE TABLE IF NOT EXISTS [{task_id}](notification TEXT)")
        for notification in notifications:
            with self.conn:
                self.curs.execute(f"INSERT INTO [{task_id}] (notification) VALUES(?);", (notification,))

        logger.log("Editing Task")

    # deletes a task in the sqlite database
    def delete_task(self, task_id: str) -> None:
        '''
        removes task from the list
        '''

        #deletes row in tasks table
        with self.conn:
            self.curs.execute(f"DELETE FROM tasks WHERE id_number='{task_id}';")

        #deletes notifcation table for task
        with self.conn:
            self.curs.execute(f"DROP TABLE IF EXISTS [{task_id}];")

        # logs
        logger.log("Deleted Task")



    # returns a list of lists, each list in the list is a task's data (add decorators in the future for this, or something idk just make it look less trash)
    def get_tasks(self, order: str ='da') -> List[List[str, str, datetime, datetime]]:

        def get_by_alphabetic():
            self.curs.execute("SELECT * FROM tasks ORDER BY task_name")
            logger.log("Sorted Alphabetically")

        def get_by_time_remaining_asc():
            self.curs.execute("SELECT * FROM tasks ORDER BY DATETIME(time_due) DESC")
            logger.log("Sorted by Time")

        def get_by_time_remaining_desc():
            self.curs.execute("SELECT * FROM tasks ORDER BY DATETIME(time_due) ASC")
            logger.log("Sorted by Reverse Time")
        
        def get_by_date_added():
            self.curs.execute("SELECT * FROM tasks ORDER BY DATETIME(time_made) ASC")
            logger.log("Sorted by Add Date")

        with self.conn:
            if order=='alpha':
                get_by_alphabetic()
            elif order=='tra':
                get_by_time_remaining_asc()
            elif order=='trd':
                get_by_time_remaining_desc()
            else:
                get_by_date_added()

            all_tasks = self.curs.fetchall()
            return [[task[0], task[1], datetime.strptime(task[2], "%m-%d-%Y, %H:%M:%S"), datetime.strptime(task[3], "%m-%d-%Y, %H:%M:%S")] for task in all_tasks]

    # returns a list of a task's data
    def get_task(self, task_id: str) -> List[str, str, datetime, datetime]:

        with self.conn:
            self.curs.execute(f"SELECT * FROM tasks WHERE id_number='{task_id}';")
            task = self.curs.fetchall()[0]
            return [task[0], task[1], datetime.strptime(task[2], "%m-%d-%Y, %H:%M:%S"), datetime.strptime(task[3], "%m-%d-%Y, %H:%M:%S")]

    # returns a list of datetimes
    def get_notifications(self, task_id: str) -> List[str]:

        with self.conn:
            self.curs.execute(f"SELECT * FROM [{task_id}]")
            notifications = self.curs.fetchall()
            return [notification[0] for notification in notifications]



    # notifies all tasks in datbase 
    def notify_tasks(self) -> None:
        
        with self.conn:
            self.curs.execute("SELECT id_number FROM tasks")
            tasks_list = self.curs.fetchall() 

        for task_id in tasks_list:
            notifications = self.get_notifications(task_id[0])
            for notification in notifications:
                if datetime.now().time().strftime("%H:%M:%S") == (datetime.strptime(notification, "%I:%M %p").time()).strftime("%H:%M:%S"):
                    self.notify('your thing is due eventually')

    # notifies single task
    def notify_task(self, task_id: str, message: str) -> None:
        self.notify(message)

    # custom notification
    def notify(self, message: str) -> None:
        notifier.show_toast(
            'test',
            'message',
            icon_path=None,
            duration=5,
            threaded=True
            )


