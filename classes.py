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

    def add_task(self, task_name="Untitled", time_due="Jan 1, 2099", time_made=datetime.today(), id_number=int(uuid.uuid4())):
        '''
         adds a task with parameters, uses today as default time_made parameter
        '''
        # creates a Task object with params
        self.tasks_list.append(Task(task_name, time_due, time_made, id_number)) 
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
            if task.id_number == task_id:

                task.edit_task(name_change, date_change)
                logger.log("Changing Name")
                logger.log("Changing Date")
                self.save()
                return
    
    def delete_task(self, task_id):
        '''
        removes task from the list
        '''

        for task in self.tasks_list:
            if task.id_number == task_id:
                self.tasks_list.remove(task)
                
        self.save()

    def save(self):

        to_save = []

        for task in self.tasks_list:
            to_save.append(task.get_dict())

        save_location = os.path.dirname(os.path.abspath(__file__))
        saver = os.path.join(save_location, "save_files.txt")

        json_dump = json.dumps(to_save)

        with open(saver, "w+") as handle:
            print(json_dump, file=handle, end="")

    def load(self):

        save_location = os.path.dirname(os.path.abspath(__file__))
        save_file = os.path.join(save_location, "save_files.txt")

        with open(save_file, "r") as handle:
            first = handle.read()
            if not first:
                logger.log("No Save Found")

            elif first:
                logger.log("Save Found")
                logger.log("User Data Retrieved")
                
                tasks_list = json.loads(first)

                for task in tasks_list:
                   self.add_task(task['task name'], datetime.strptime(task['due date'], "%m-/%d-/%Y, %H:%M:%S"), datetime.strptime(task['date created'], "%m-/%d-/%Y, %H:%M:%S"), task["task id"])

class Task(object):

    def __init__(self, task_name, time_due, time_made, id_number):

        self.task_name = task_name
        self.time_due = time_due
        self.time_made = time_made
        self.id_number = id_number

    def edit_task(self, new_task_name, new_due_date):

        self.task_name = new_task_name
        self.time_due = new_due_date

    def display_task(self):
        
        print("task name: " + self.task_name)
        print("due date: " + str(self.time_due))
        print("date created: " + str(self.time_made))
        print("task id: " + str(self.id_number))

    def get_dict(self):

        le_dict = {
            "task name" :  self.task_name,
            "due date" :  self.time_due.strftime("%m-/%d-/%Y, %H:%M:%S"),
            "date created" :  self.time_made.strftime("%m-/%d-/%Y, %H:%M:%S"),
            "task id" :  self.id_number
        }
        return le_dict

        