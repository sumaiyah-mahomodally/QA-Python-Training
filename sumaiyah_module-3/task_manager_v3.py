# Version 3 - Using Functions

def display_tasks(tasks):
    """Display all tasks"""

    if len(tasks) == 0:
        print("Your task list is empty.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['description']} [{task['status']}]")

    print("------------------")


def add_task(tasks):
    """Add a new task"""

    description = input("Enter task description: ")

    if description.strip() == "":
        print("Task description cannot be empty.")
        return

    task = {
        "description": description,
        "status": "pending"
    }

    tasks.append(task)

    print(f'Added: "{description}"')


def mark_task_complete(tasks):
    """Mark a task as completed"""

    if len(tasks) == 0:
        print("No tasks to mark.")
        return

    display_tasks(tasks)

    task_number = input("Enter task number: ")

    if not task_number.isdigit():
        print("Please enter a valid number.")
        return

    task_index = int(task_number) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[task_index]["status"] = "completed"

    print(
        f'Marked "{tasks[task_index]["description"]}" as completed.'
    )


def main():

    tasks = []

    while True:

        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
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
