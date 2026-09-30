# Exercise 2 - Dictionary Practice

tester = {
    "name": "Sumaiyah",
    "role": "QA Engineer Associate",
    "project": "Python Training"
}

print("Name:", tester["name"])
print("Role:", tester["role"])
print("Project:", tester["project"])

# Add a new key
tester["location"] = "Mauritius"

print("\nUpdated Dictionary:")
print(tester)

# Missing key example
try:
    print(tester["experience"])
except KeyError:
    print("\nKeyError: experience does not exist")

# Using get()
print("\nUsing get():")
print(tester.get("experience", "Not provided"))
