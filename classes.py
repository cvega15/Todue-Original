import time
from datetime import datetime
import timeit
import logger 
import utils  
import os                                          
import json
import random

#this is used for storing a list of tasks as well as adding them
class User_tasks(object):

    # whole init needs redoing with main for the save functionality
    def __init__(self, task_list):                                           #constructor
        
        self.tasks_list = list(task_list)                                      #the tasks list which holds an array of tasks - for starting, this needs to be initialized if save file found
        logger.log("User_Tasks Created")

        if self.tasks_list: # checks if the task has anything to open from the save file
            self.deserialize()

    def add_task(self, id_number=random.randint(0, 1000), task_name="Untitled", time_due="Jan 1, 2099"):  # adds a task with information passed into the parameters
        
        self.tasks_list.append({"id": id_number, "task_name": task_name, "time_due": time_due})
        self.save()
        logger.log("Adding Task")

    def display_tasks(self):                                      #displays all of the tasks and their information
        
        for task in self.tasks_list:
            print(task)

        logger.log("Displaying Tasks")
    
    def edit_task(self, task_id, name_change, date_change):     # calls the edit_name and edit_due_date functions with parameters passed in

        for task in self.tasks_list:
            if task_id in task:

                task['task_name'] = name_change
                logger.log("Changing Name")
                task['time_due'] = date_change
                logger.log("Changing Date")

        self.save()
    
    def delete_task(self, task_id):
        
        for task in self.tasks_list:
            if task_id in task:
                del task

        self.save()

    def serialize(self):

        serialized_task_list = []

        for task in self.tasks_list:
            serialized_task_list.append(task.serialize())
        self.json_dump = json.dumps(serialized_task_list)

        logger.log("Serialized")   
    
    def save(self):

        location = os.path.dirname(os.path.abspath(__file__))
        saver = os.path.join(location, "save_files.txt")
        with open(saver, "w+") as handle:
            print(self.json_dump, file=handle, end="")

        logger.log("User Data Saved")
    
    def deserialize(self):
        # write the json.loads(string) on the main.py under loading at the bottom
        logger.log("User Data Retrieved")
        task_temp = []

        for item in self.tasks_list:
            task_temp.append(item)

        self.tasks_list = task_temp

#   test      # 
# x = Timer("2019-07-12 9:00:00")
# print(x.timer_display())
