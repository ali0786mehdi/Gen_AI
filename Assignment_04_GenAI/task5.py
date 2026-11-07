# Assignment 4 - Task 5: Create Product Info File (User Input)

# Ask the user for 3 product names and their prices
products = []
prices = []

for number in range(1, 4):
    name = input("Enter name of product " + str(number) + ": ")

    price = input("Enter price of " + name + ": ")
    # Keep asking until the price is a valid number
    while not price.replace(".", "", 1).isdigit():
        print("Invalid price, please enter a number.")
        price = input("Enter price of " + name + ": ")

    products.append(name)
    prices.append(price)

# Write them in the format: ProductName | Price
with open("products.txt", "w") as file:
    for i in range(len(products)):
        file.write(products[i] + " | " + prices[i] + "\n")

# Read the file and print each line
print()
print("Contents of products.txt:")
with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())
