import os

directory_path = '/'
contents = os.listdir(directory_path)

print(f"Contents of the directory '{directory_path}':")
for item in contents:
    print(item)