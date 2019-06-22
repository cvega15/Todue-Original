import logger 
import os                                          
import json
import time
import uuid
from threading import Timer
from datetime import datetime

#this is used for storing a list of tasks as well as adding them
class User_tasks(object):

    # whole init needs redoing with main for the save functionality
    def __init__(self): 
        # creates task list which holds the tasks and loads the tasks if there are any
        self.tasks_list = []
        self.load()

        logger.log("User_Tasks Created")

    def add_task(self, id_number=uuid.uuid4(), task_name="Untitled", time_due="Jan 1, 2099", time_made=datetime.today()):
        '''
         adds a task with parameters, uses today as default time_made parameter
        '''
        # creates a Task object with params
        self.tasks_list.append(Task(id_number, task_name, time_due, time_made)) 
        self.save()
        logger.log("Adding Task")

    def display_tasks(self):
        '''
        displays tasks and their featues
        '''
        
        for task in self.tasks_list:
            task.display_task()

        logger.log("Displaying Tasks")
    
    def edit_task(self, task_id, name_change, date_change):
        '''
        calls the edit_name and edit_due_date functions with parameters passed in
        '''

        for task in self.tasks_list:
            if task.task_id == task['id']:
                task.task_name = name_change
                logger.log("Changing Name")
                task.time_due = date_change
                logger.log("Changing Date")

        self.save()
    
    def delete_task(self, task_id):
        '''
        removes task from the list
        '''

        for task in self.tasks_list:
            if task.task_id == task['id']:
                self.tasks_list.remove(task)
                
        self.save()

    def serialize(self):

        # creates the json format for saving
        self.json_dump = json.dumps(self.tasks_list) 

        logger.log("Serialized")   
    
    def save(self):
        '''
        finds the location of the file and prints the json format into the file
        '''
        self.serialize()
        save_location = os.path.dirname(os.path.abspath(__file__))
        saver = os.path.join(save_location, "save_files.txt")
        with open(saver, "w+") as handle:
            print(self.json_dump, file=handle, end="")

        logger.log("User Data Saved")

    def load(self):
        '''
        reads the file and decodes the json into the tasks_list
        '''
        save_location = os.path.dirname(os.path.abspath(__file__))
        save_file = os.path.join(save_location, "save_files.txt")

        with open(save_file, "r") as handle:
            first = handle.read()
            if not first:
                logger.log("No Save Found")

            elif first:
                logger.log("Save Found")
                logger.log("User Data Retrieved")
                self.tasks_list = json.loads(first)

class Task(object):

    def __init__(self, id_number, task_name, time_due, time_made):

        self.id_number = id_number
        self.task_name = task_name
        self.time_due = time_due
        self.time_made = time_made

    def edit_task(self, new_task_name, new_due_date):

        self.task_name = new_task_name
        self.time_due = new_due_date

    def display_task(self):
        
        print("task id: " + str(self.id_number))
        print("task name: " + self.task_name)
        print("due date: " + str(self.time_due))
        print("date created: " + str(self.time_made))

