import logger 
import os                                          
import time
import sqlite3
from datetime import datetime
from datetime import time
from operator import itemgetter
from typing import List, Tuple


#this is used for storing a list of tasks as well as adding them
class TaskCollection(object):

    # constructor
    def __init__(self, user_id):
        
        self.user_id = user_id

        #creates a connection to the database and creates a database file
        self.conn = sqlite3.connect('user_data.db')
        self.curs = self.conn.cursor()

        #creates a table to hold tasks if one doesn't exist
        with self.conn:
            self.curs.execute("CREATE TABLE IF NOT EXISTS tasks(id_number TEXT, task_name TEXT, time_due TEXT, time_made TEXT, notifications TEXT, user_id INT)")
        
        logger.log("TaskCollection Created")



    # adds a task to the sqlite database 
    def add_task(self, task_name: str, time_due: datetime, time_made: datetime, id_number: str, notifications: List[datetime.time] = []) -> None:
        '''
        adds a task with parameters, uses today as default time_made parameter
        '''

        # new sqlite stuff
        with self.conn:
            self.curs.execute("INSERT INTO tasks(id_number, task_name, time_due, time_made, notifications) VALUES(:id, :name, :time_due, :time_made, :notifications, :user_id)", 
            {'id':id_number, 
             'name':task_name, 
             'time_due':time_due.strftime('%m-%d-%Y, %H:%M:%S'), 
             'time_made':time_made.strftime('%m-%d-%Y, %H:%M:%S'), 
             'notifications':self.serialize_notifications(notifications), 
             'user_id':self.user_id})

        print(self.serialize_notifications(notifications))
        logger.log("Adding Task")

    # edits a task in the sqlite database
    def edit_task(self, task_id: str, name_change: str, date_change: datetime, notifications: List[datetime.time] = []) -> None:
        '''
        calls the edit_name and edit_due_date functions with parameters passed in
        '''

        #edits the task row in the tasks table
        with self.conn:
            self.curs.execute(f"UPDATE tasks SET task_name = :name, time_due = :time_due, notifications = :notifications WHERE id_number = :id", 
            {'name':name_change, 'time_due':date_change.strftime('%m-%d-%Y, %H:%M:%S'), 'notifications':self.serialize_notifications(notifications), 'id':task_id})

        logger.log("Editing Task")

    # deletes a task in the sqlite database
    def delete_task(self, task_id: str) -> None:
        '''
        removes task from the list
        '''

        #deletes row in tasks table
        with self.conn:
            self.curs.execute(f"DELETE FROM tasks WHERE id_number='{task_id}';")

        # logs
        logger.log("Deleted Task")



    # returns a list of lists, each list in the list is a task's data (add decorators in the future for this, or something idk just make it look less trash if possible)
    def get_tasks(self, order: str = 'da') -> List[Tuple[str, str, datetime, datetime]]:

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
            if order == 'alpha':
                get_by_alphabetic()
            elif order == 'tra':
                get_by_time_remaining_asc()
            elif order =='trd':
                get_by_time_remaining_desc()
            else:
                get_by_date_added()

            all_tasks = self.curs.fetchall()
            return [[task[0], task[1], datetime.strptime(task[2], "%m-%d-%Y, %H:%M:%S"), datetime.strptime(task[3], "%m-%d-%Y, %H:%M:%S"), self.deserialize_notifications(task[4])] for task in all_tasks]

    # returns a list of a task's data
    def get_task(self, task_id: str) -> Tuple[str, str, datetime, datetime]:

        with self.conn:
            self.curs.execute(f"SELECT * FROM tasks WHERE id_number='{task_id}';")
            task = self.curs.fetchall()[0]
            return [task[0], task[1], datetime.strptime(task[2], "%m-%d-%Y, %H:%M:%S"), datetime.strptime(task[3], "%m-%d-%Y, %H:%M:%S"), self.deserialize_notifications(task[4])]

    # 
    def get_notifications(self, task_id: str) -> List[datetime.time]:

        with self.conn:
            self.curs.execute(f"SELECT notifications FROM tasks WHERE id_number = '{task_id}'")
            return self.deserialize_notifications(self.curs.fetchall()[0][0])



    #
    def serialize_notifications(self, times: List[datetime.time] = []) -> str:

        return str([time.strftime('%H:%M') for time in times])[1:-1]

    # takes in a "list" of strings and returns a list of datetimes
    def deserialize_notifications(self, times: str) -> List[datetime.time]:

        if times == '':
            return []

        new_times = times.split(',')
        return [datetime.strptime(time.lstrip()[1:-1], '%H:%M').time() for time in new_times]


