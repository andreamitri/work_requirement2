# Exercise 2 – Task List Manager
import tasks

task_list = []

while True:
    command = input("Enter command (add, remove, done): ")

    if command == "done":
        break

    elif command.startswith("add "):
        task = command[4:]
        tasks.add_task(task_list, task)

    elif command.startswith("remove "):
        task = command[7:]
        tasks.remove_task(task_list, task)

    print("Current tasks:", task_list)
