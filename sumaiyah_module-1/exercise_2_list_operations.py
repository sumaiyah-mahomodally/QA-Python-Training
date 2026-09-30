# Exercise 2

tasks = [
    "Task 1",
    "Task 2",
    "Task 3",
    "Task 4",
    "Task 5"
]

print("First task:", tasks[0])
print("Last task:", tasks[-1])

print("Number of tasks:", len(tasks))

tasks.append("Task 6")

print("\nAfter append:")
print(tasks)
print("New length:", len(tasks))

try:
    print(tasks[10])
except IndexError:
    print("IndexError: list index out of range")
