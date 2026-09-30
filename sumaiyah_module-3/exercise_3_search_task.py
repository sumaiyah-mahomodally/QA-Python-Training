def search_tasks(tasks, keyword):

    results = []

    for task in tasks:

        if keyword.lower() in task["description"].lower():
            results.append(task)

    return results


tasks = [
    {"description": "Learn Python", "status": "pending"},
    {"description": "Python Training Exercise", "status": "pending"},
    {"description": "Read a Book", "status": "completed"}
]

matches = search_tasks(tasks, "python")

print("Search Results:")

for task in matches:
    print(f"{task['description']} [{task['status']}]")
