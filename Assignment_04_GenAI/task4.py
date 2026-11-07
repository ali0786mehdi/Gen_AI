# Assignment 4 - Task 4: Generate Summary Report from File
# (Run task1.py and task3.py first)

sales = []

# Read all sales values from the file and convert them to integers
with open("sales_data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line != "":
            sales.append(int(line))

total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

print("===== Sales Summary Report =====")
print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", round(average_sale, 2))
