import classes
import logger

logger.start()
user_tasks = classes.User_tasks()

print("hello, le task scheduling program has arrived! this'll be ebic")         #is this so ppl who view this understand its a meme? ----->      #meme

while True:
    print("1) add task \n2) display tasks \n3) edit task\n4) quit")
    user_input = int(input('>'))

    if user_input == 1:
        logger.log("User Create New Task")

        task_name = input('please enter in a task name: \n>')
        due_date = input('now make up a due date: \n>')
        user_tasks.add_task(task_name, due_date)
        
    elif user_input == 2:
        logger.log("User Display Task")

        user_tasks.display_tasks()

    elif user_input == 3:
        logger.log("User editing task")
        user_tasks.display_tasks()

        to_edit = input('please enter in the name of the task that you want to edit: \n>')
        edit_selection = int(input('1) rename task \n2) change due date \n3) cancel: \n>'))

        if(edit_selection == 1):
            name_change = input('enter name change: \n>')
            user_tasks.edit_task(to_edit, name_change, None)

            logger.log("name changed")

        elif(edit_selection == 2):
            date_chage = input('enter date change: \n>')
            user_tasks.edit_task(to_edit, None, date_chage)

            logger.log("date changed")

        else:
            break



    else:
        print('quitting')
        break

logger.log("End--------------------------------------------------")
