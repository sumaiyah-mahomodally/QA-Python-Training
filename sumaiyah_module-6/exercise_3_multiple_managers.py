class TaskManager:

    def __init__(self, filename):
        self.filename = filename

    def display(self):
        print(f"Managing file: {self.filename}")


work = TaskManager("work.json")
personal = TaskManager("personal.json")

work.display()
personal.display()
