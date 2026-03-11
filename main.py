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

# Exercise 3 – Simple Class and Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student = Student("Anna", 22, "S12345")
student.greet()
print("Student ID:", student.student_id)