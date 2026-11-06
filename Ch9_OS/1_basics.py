import os

# print(os.getcwd()) # Get current working directory

# print(os.path.abspath(__file__)) # Get the absolute path of the current file

# print(os.path.dirname(os.path.abspath(__file__))) # Get the directory name of the current file

# print(os.listdir()) # List all files and directories in the current directory

# for i in os.listdir():
#     if os.path.isfile(i):
#         print(f"{i} is a file")
#     elif os.path.isdir(i):
#         print(f"{i} is a directory")

print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Data")) # List all files and directories in the Data directory

last_load = "2026-01-01 12:00:00"

for i in  os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Data")):
    if i.split(".")[0] > last_load:
     
        print(f"{i} is a new file")