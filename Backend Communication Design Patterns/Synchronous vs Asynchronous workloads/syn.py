import os

# Print the first log message
print("1\n")

# Read the file synchronously
with open("test.txt", "r") as file:
    res = file.read()

# Print the file contents with a newline after
print(f"file: {res}\n")

# Print the second log message
print("2")

