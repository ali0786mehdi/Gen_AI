# Assignment 3 - Task 7: Mini Problem - Menu Using Functions

def add_price(prices_list, price):
    prices_list.append(price)


def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list)


def get_max_price(prices_list):
    return max(prices_list)


prices_list = []

while True:
    print()
    print("===== Price Menu =====")
    print("1 - Add price")
    print("2 - Show average price")
    print("3 - Show highest price")
    print("q - Quit")

    choice = input("Choose an option: ").lower()

    if choice == "1":
        text = input("Enter a price: ")
        # Allow whole numbers and numbers with one decimal point
        if text.replace(".", "", 1).isdigit():
            add_price(prices_list, float(text))
            print("Price added.")
        else:
            print("Invalid price, please enter a number.")

    elif choice == "2":
        if len(prices_list) == 0:
            print("No prices added yet.")
        else:
            print("Average price:", round(get_average_price(prices_list), 2))

    elif choice == "3":
        if len(prices_list) == 0:
            print("No prices added yet.")
        else:
            print("Highest price:", get_max_price(prices_list))

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
