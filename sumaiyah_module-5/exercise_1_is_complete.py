class Task:

    def __init__(self, description, status="pending"):
        self.description = description
        self.status = status

    def is_complete(self):

        return self.status == "completed"


task1 = Task("Learn Python")
task2 = Task("Complete QA Training", "completed")

print(task1.is_complete())
print
