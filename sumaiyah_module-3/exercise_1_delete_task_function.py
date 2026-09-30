def delete_task(tasks):

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['description']}")

    task_number = input("Enter task number to delete: ")

    if task_number.isdigit():

        task_index = int(task_number) - 1

        if 0 <= task_index < len(tasks):

            removed = tasks.pop(task_index)

            print(f'Deleted: "{removed["description"]}"')

        else:
            print("Invalid task number.")

    else:
        print("Please enter a valid number.")


tasks = [
    {"description": "Learn Python", "status": "pending"},
    {"description": "Read Book", "status": "completed"}
]

delete_task(tasks)
