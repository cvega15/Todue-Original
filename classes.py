import logger 
import os                                          
import json
import random

#this is used for storing a list of tasks as well as adding them
class User_tasks(object):

    # whole init needs redoing with main for the save functionality
    def __init__(self):                                           #constructor

        self.tasks_list = []                                      #the tasks list which holds an array of tasks - for starting, this needs to be initialized if save file found
        logger.log("User_Tasks Created")

        self.retrieve()

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

        self.json_dump = json.dumps(self.tasks_list)

        logger.log("Serialized")   
    
    def save(self):

        self.serialize()
        save_location = os.path.dirname(os.path.abspath(__file__))
        saver = os.path.join(save_location, "save_files.txt")
        with open(saver, "w+") as handle:
            print(self.json_dump, file=handle, end="")

        logger.log("User Data Saved")

    def retrieve(self):
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
