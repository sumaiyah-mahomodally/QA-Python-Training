import json

TASKS_FILE = "tasks.json"


class Task:

    def __init__(self, description, status="pending"):
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.description} [{self.status}]"

    def mark_complete(self):
        self.status = "completed"

    def to_dict(self):
        return {
            "description": self.description,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["description"],
            data["status"]
        )


def load_tasks():

    try:
        with open(TASKS_FILE, "r") as file:

            tasks_data = json.load(file)

            return [
                Task.from_dict(task)
                for task in tasks_data
            ]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_tasks(tasks):

    tasks_data = [
        task.to_dict()
        for task in tasks
    ]

    with open(TASKS_FILE, "w") as file:
        json.dump(tasks_data, file, indent=4)


def display_tasks(tasks):

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n--- Tasks ---")

    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

    print("-------------")


def add_task(tasks):

    description = input("Enter task description: ")

    task = Task(description)

    tasks.append(task)

    save_tasks(tasks)

    print("Task added.")


def mark_task_complete(tasks):

    display_tasks(tasks)

    task_number = input("Enter task number: ")

    if task_number.isdigit():

        task_index = int(task_number) - 1

        if 0 <= task_index < len(tasks):

            tasks[task_index].mark_complete()

            save_tasks(tasks)

            print("Task completed.")


def main():

    tasks = load_tasks()

    while True:

        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            mark_task_complete(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()
``
