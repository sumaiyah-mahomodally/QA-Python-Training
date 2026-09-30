class Task:

    def __init__(self, description, status="pending"):
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.description} [{self.status}]"

    def mark_complete(self):
        self.status = "completed"

    def to_dict(self):
        return {
            "description": self.description,
            "status": self.status
