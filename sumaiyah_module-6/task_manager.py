import json


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


class TaskManager:

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):

        try:
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)

            self.tasks = [
                Task.from_dict(task)
                for task in tasks_data
            ]

        except FileNotFoundError:
            self.tasks = []

        except json.JSONDecodeError:
            self.tasks = []

    def save_tasks(self):

        tasks_data = [
            task.to_dict()
            for task in self.tasks
        ]

        with open(self.filename, "w") as file:
            json.dump(tasks_data, file, indent=4)

    def add_task(self, description):

        task = Task(description)

        self.tasks.append(task)

        self.save_tasks()

        print("Task added.")

    def view_tasks(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def mark_task_complete(self, task_number):

        task_index = int(task_number) - 1

        if 0 <= task_index < len(self.tasks):

            self.tasks[task_index].mark_complete()

            self.save_tasks()

            print("Task completed.")

    def run(self):

        while True:

            print("\n1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                description = input("Enter task: ")

                self.add_task(description)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":

                self.view_tasks()

                task_number = input("Enter task number: ")

                self.mark_task_complete(task_number)

            elif choice == "4":

                print("Goodbye!")

                break

            else:
                print("Invalid choice")


if __name__ == "__main__":

    app = TaskManager()

    app.run()
