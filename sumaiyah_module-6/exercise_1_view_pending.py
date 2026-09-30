class Task:

    def __init__(self, description, status):
        self.description = description
        self.status = status


tasks = [
    Task("Learn Python", "pending"),
    Task("Read Book", "completed"),
    Task("Finish Training", "pending")
]

print("Pending Tasks:")

for task in tasks:

    if task.status == "pending":
        print(task.description)
