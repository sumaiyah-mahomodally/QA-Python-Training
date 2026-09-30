def is_empty(tasks):

    return len(tasks) == 0


tasks = []

if is_empty(tasks):
    print("Task list is empty")
else:
    print("Task list contains tasks")
