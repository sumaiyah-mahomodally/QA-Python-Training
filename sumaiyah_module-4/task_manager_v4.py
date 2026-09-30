import json

TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n--- Tasks ---")

    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['description']} [{task['status']}]")

    print("-------------")


def add_task(tasks):

    description = input("Enter task description: ")

    task = {
        "description": description,
        "status": "pending"
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully.")


def main():

    tasks = load_tasks()

    while True:

        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":

            save_tasks(tasks)

            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()
