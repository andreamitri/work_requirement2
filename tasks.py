def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added.")


def remove_task(task_list, task):
    try:
        task_list.remove(task)
        print(f"Task '{task}' removed.")
    except ValueError:
        print("Task not found.")