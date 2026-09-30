class Task:

    def __init__(self, description):
        self.description = description


class DeadlineTask(Task):

    def __init__(self, description, due_date):

        super().__init__(description)

        self.due_date = due_date


task = DeadlineTask(
    "Submit Python Assignment",
    "2026-10-15"
)

print(task.description)
print(task.due_date)
