import classes
import logger

logger.start()
user_tasks = classes.User_tasks()

print("hello, le task scheduling program has arrived!")         #      #meme

while True:
    print("1) add task \n2) display tasks \n3) quit")
    user_input = int(input('>'))

    if user_input == 1:
        logger.log("User Create New Task")

        task_name = input('please enter in a task name: \n>')
        due_date = input('now make up a due date: \n>')
        user_tasks.add_task(task_name, due_date)
        

    elif user_input == 2:
        logger.log("User Display Task")

        user_tasks.display_tasks()

    else:
        break

logger.log("End--------------------------------------------------")
