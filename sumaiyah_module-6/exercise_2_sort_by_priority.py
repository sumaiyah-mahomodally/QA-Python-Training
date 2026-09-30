tasks = [
    {"description": "Task A", "priority": "medium"},
    {"description": "Task B", "priority": "high"},
    {"description": "Task C", "priority": "low"}
]

priority_order = {
    "high": 0,
    "medium": 1,
    "low": 2
}

sorted_tasks = sorted(
    tasks,
    key=lambda task: priority_order[task["priority"]]
)

for task in sorted_tasks:
    print(task)
