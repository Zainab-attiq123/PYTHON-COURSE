import os

# Specify the directory path you want to list
directory_path = "/path/to/your/directory"

# Use os.listdir() to get the contents
contents = os.listdir(directory_path)

# Print the contents
print(f"Contents of the directory '{directory_path}':")
for item in contents:
    print(item)