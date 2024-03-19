
import os
from datetime import datetime

class MyTask:
    def __init__(self, title, priority='low', due_date=None, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"Task: {self.title}\nPriority: {self.priority}\nDue Date: {self.due_date}\nStatus: {status}\n"

class MyToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks[:]:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                return True
        return False

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def get_all_tasks(self):
        return self.tasks

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title}|{task.priority}|{task.due_date}|{task.completed}\n")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    title, priority, due_date, completed = line.strip().split('|')
                    due_date = datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
                    completed = completed == 'True'
                    task = MyTask(title, priority, due_date, completed)
                    self.add_task(task)

def start():
    filename = "my_tasks.txt"
    my_todo_list = MyToDoList()
    my_todo_list.load_from_file(filename)

    while True:
        print("\n1. Add New Task")
        print("2. Remove a Task")
        print("3. Mark Task as Done")
        print("4. Show All Tasks")
        print("5. Remove All Tasks")
        print("6. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Priority (high/medium/low): ")
            while priority.lower() not in ['high', 'medium', 'low']:
                print("Invalid priority. Please choose 'high', 'medium', or 'low'.")
                priority = input("Priority (high/medium/low): ")
            due_date_str = input("Due date (YYYY-MM-DD), press enter if none: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
            task = MyTask(title, priority, due_date)
            my_todo_list.add_task(task)
            my_todo_list.save_to_file(filename)
            print("Task added.")

        elif choice == '2':
            title = input("Enter task title to remove: ")
            if my_todo_list.remove_task(title):
                my_todo_list.save_to_file(filename)
                print("Task removed.")
            else:
                print("Task not found.")

        elif choice == '3':
            title = input("Enter task title to mark as done: ")
            if my_todo_list.mark_task_done(title):
                my_todo_list.save_to_file(filename)
                print("Task marked as done.")
            else:
                print("Task not found.")

        elif choice == '4':
            tasks = my_todo_list.get_all_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks.")

        elif choice == '5':
            confirmation = input("Are you sure you want to remove all tasks? (yes/no): ")
            if confirmation.lower() == 'yes':
                my_todo_list.tasks = []  
                my_todo_list.save_to_file(filename)
                print("All tasks removed.")
            else:
                print("Operation canceled.")

        elif choice == '6':
            print("Exiting.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    start()