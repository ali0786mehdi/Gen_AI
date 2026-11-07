# Assignment 4 - Task 6: Read File Safely

import os

filename = input("Enter the filename to open: ")

# Check if the file exists before opening it
if os.path.exists(filename):
    with open(filename, "r") as file:
        print()
        print("Contents of " + filename + ":")
        print(file.read())
else:
    print("File not found. Please check the filename.")
