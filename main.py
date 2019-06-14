import classes

user_tasks = classes.tasks()

print("hello, welcome to le task scheduling program!")

while True:

    print("1) add task\n2) display tasks\n3) quit")
    user_input = int(input('>'))

    if(user_input == 1):
        task_name = input('please enter in a task name: ')
        due_date = input('now make up a due date: ')
        user_tasks.add_task(task_name, due_date)

    elif(user_input == 2):
        user_tasks.display_tasks()

    else:
        break

print('program finished')