# Assignment 4 - Task 2: Read File in Different Ways
# (Run task1.py first so that sales_data.txt exists)

# 1. Read the entire file using read()
with open("sales_data.txt", "r") as file:
    whole_file = file.read()

print("Using read():")
print(whole_file)

# 2. Read only the first line using readline()
with open("sales_data.txt", "r") as file:
    first_line = file.readline()

print("Using readline():")
print(first_line.strip())      # strip() removes the newline character
print()

# 3. Read all lines using readlines() and convert them to integers
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

sales = []
for line in lines:
    line = line.strip()
    if line != "":
        sales.append(int(line))

print("Using readlines() converted to integers:")
print(sales)
