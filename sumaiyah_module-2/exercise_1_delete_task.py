# Exercise 1 - Delete Task

tasks = [
    {"description": "Learn Python", "status": "pending"},
    {"description": "Read a book", "status": "pending"},
    {"description": "Go shopping", "status": "completed"}
]

print("\nCurrent Tasks:")

for index, task in enumerate(tasks):
    print(f"{index + 1}. {task['description']} [{task['status']}]")

task_number = input("\nEnter task number to delete: ")

if task_number.isdigit():

    task_index = int(task_number) - 1

    if 0 <= task_index < len(tasks):

        removed = tasks.pop(task_index)

        print(f'\nDeleted: "{removed["description"]}"')

    else:
        print("Invalid task number.")

else:
    print("Please enter a valid number.")

print("\nRemaining Tasks:")

for index, task in enumerate(tasks):
    print(f"{index + 1}. {task['description']} [{task['status']}]")
