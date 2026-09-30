# Version 2: Menu-driven Task Manager

tasks = []

print("=== Task Manager ===\n")

while True:

    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":

        description = input("Enter the task description: ")

        task = {
            "description": description,
            "status": "pending"
        }

        tasks.append(task)
        print(f'Added: "{description}"')

    elif choice == "2":

        if len(tasks) == 0:
            print("Your task list is empty.")

        else:
            print("\n--- Your Tasks ---")

            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['description']} [{task['status']}]")

            print("------------------")

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to mark.")

        else:

            print("\n--- Your Tasks ---")

            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['description']} [{task['status']}]")

            task_number = input("Enter task number: ")

            if task_number.isdigit():

                task_index = int(task_number) - 1

                if 0 <= task_index < len(tasks):

                    tasks[task_index]["status"] = "completed"

                    print(
                        f'Marked "{tasks[task_index]["description"]}" as completed.'
                    )

                else:
                    print("Invalid task number.")

            else:
                print("Enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
