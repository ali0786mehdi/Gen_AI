# Assignment 4 - Task 3: Append New Sales
# (Run task1.py first. Running this file again will append the values again.)

new_sales = [5000, 2500, 1700]

# Open in append mode so the old data is kept
with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")

# Reopen and print the whole updated file
with open("sales_data.txt", "r") as file:
    content = file.read()

print("Updated sales_data.txt:")
print(content)

# Extra (optional): print the total number of lines
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))
