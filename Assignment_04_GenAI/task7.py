# Assignment 4 - Task 7: Mini Project - Export Discounted Prices

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask the user for a discount percentage (0 to 100)
discount_text = input("Enter discount percentage: ")
while not discount_text.replace(".", "", 1).isdigit() or float(discount_text) > 100:
    print("Invalid discount, enter a number between 0 and 100.")
    discount_text = input("Enter discount percentage: ")

discount = float(discount_text)

total_items = 0
total_discounted = 0

# Write the report file
with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")

    for product in prices:
        original = prices[product]
        discounted = round(original - (original * discount / 100), 2)

        file.write(product + " | " + str(original) + " | " + str(discounted) + "\n")

        total_items = total_items + 1
        total_discounted = total_discounted + discounted

    # Extra (optional): summary at the bottom of the file
    average_discounted = round(total_discounted / total_items, 2)
    file.write("\n")
    file.write("Total Items: " + str(total_items) + "\n")
    file.write("Average Discounted Price: " + str(average_discounted) + "\n")

# Read the file and print it to the terminal
print()
print("Contents of discount_report.txt:")
with open("discount_report.txt", "r") as file:
    print(file.read())
