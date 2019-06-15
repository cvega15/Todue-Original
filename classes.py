import time
from datetime import datetime
import timeit
import logger 
import utils                                                  # see logger module


#this is used for storing a list of tasks as well as adding them
class User_tasks(object):

    def __init__(self):                                           #constructor

        self.tasks_list = []                                      #the tasks list which holds an array of tasks
        logger.log("User_Tasks Created")

    def add_task(self, task_name="Untitled", time_due="Jan 1, 2099"):  # adds a task with information passed into the parameters

        task_to_add = Task(task_name, time_due)
        self.tasks_list.append(task_to_add)

        logger.log("Adding Task")

    def display_tasks(self):                                      #displays all of the tasks and their information

        for task in self.tasks_list:
            task.display_task()

        logger.log("Displaying Tasks")
    
    def edit_task(self, task_name, name_change, date_change):     # calls the edit_name and edit_due_date functions with parameters passed in

        for task in self.tasks_list:
            if task.name == task_name:

                if name_change:
                    task.edit_name(name_change)
                    return

                if date_change:
                    task.edit_due_date(date_change)
                    return
    
    def save(self):

        logger.log("User Data Saved")
    
    def retireive(self):

        logger.log("User Data Retrieved")


#a task class which holds information about it's name as well as it's due date
class Task(object):

    def __init__(self, name="Untitled", due_date="Jan 1, 2099"):                                           #constructor

        self.name = name                                          #name of the task
        self.due_date = Timer(due_date)                           #datetime object of when it's due

    def edit_name(self, new_name):                                #edits the string name of the task and changes it to the name_add passed in
        self.name = new_name

    def edit_due_date(self, new_date):                            #edits the due date of the task which is a datetime object
        self.due_date = new_date
    
    def display_task(self):                                       #displays the task -- This will be eventually passed to the display class

        print("task name: " + str(self.name))
        print("due date: " + str(self.due_date.date))


class Timer(object):

    def __init__(self, date):
        self.date = date
    
    def convert(self): # takes the date passed in and converts it to readable format for date_diff()
        pass

    def date_diff(self):

        dt = datetime.datetime
        now = dt.now()
        return dt(year=self.date, month=self.date, day=self.date, minute=self.date) - dt(year=now.year, month=now.month, day=now.day, minute=now.minute) # will need a way to differentiate days, hours, minutes