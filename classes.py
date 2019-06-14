import datetime


#this is used for storing a list of tasks as well as adding them
class tasks:

    def __init__(self):                                           #constructor
        self.tasks_list = []                                      #the tasks list which holds an array of tasks
    
    def add_task(self, task_name, time_due):                      #adds a task with information passed into the parameters

        task_to_add = task()
        task_to_add.edit_task(task_name, time_due)
        self.tasks_list.append(task_to_add)

    def display_tasks(self):                                      #displays all of the tasks and their information

        for task in self.tasks_list:
            task.display_task()



#a task class which holds information about it's name as well as it's due date
class task:

    def __init__(self):                                           #constructor

        self.name = ""                                            #name of the task
        self.due_date = ""                                        #datetime object of when it's due

    def edit_task(self, name, due_date):                          #calls the edit_name and edit_due_date functions with parameters passed in

        self.edit_name(name)
        self.edit_due_date(due_date)

    def edit_name(self, name_add):                                #edits the string name of the task and changes it to the name_add passed in
        self.name = name_add

    def edit_due_date(self, date_add):                            #edits the due date of the task which is a datetime object
        self.due_date = date_add
    
    def display_task(self):                                       #displays the task

        print(self.name)
        print(self.due_date)

