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


# Exercise 4: Math Quiz with Exception Handling
import random

def math_quiz():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    answer = input(f"What is {num1} + {num2}? ")

    try:
        answer = int(answer)

        if answer == num1 + num2:
            print("Correct!")
        else:
            print("Wrong answer.")

    except ValueError:
        print("Invalid input!")


# Simple menu to run exercises
def main():
    while True:
        print("\nChoose an exercise to run:")
        print("1 - File to List Converter")
        print("2 - Task Manager")
        print("3 - Student Class Demo")
        print("4 - Math Quiz")
        print("5 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            file_to_list()
        elif choice == "2":
            task_manager()
        elif choice == "3":
            student_demo()
        elif choice == "4":
            math_quiz()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()