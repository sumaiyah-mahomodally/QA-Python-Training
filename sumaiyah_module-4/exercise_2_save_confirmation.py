import json


def save_tasks(tasks):

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"{len(tasks)} task(s) saved successfully.")


tasks = [
    {
        "description": "Learn Python",
        "status": "pending"
    },
    {
        "description": "Complete QA Training",
        "status": "completed"
    }
]

save_tasks(tasks)
