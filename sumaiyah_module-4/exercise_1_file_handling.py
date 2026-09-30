# Exercise 1

with open("sample.txt", "w") as file:
    file.write("Hello from Python\n")
    file.write("Learning File Handling\n")

print("File written successfully.")

with open("sample.txt", "r") as file:

    content = file.read()

print("\nFile Content:")
print(content)
