# Assignment 3 - Task 6: Combined Utility Function

def process_prices(prices):
    # Apply a 10% discount to every price using map() and lambda
    discounted_prices = list(map(lambda price: round(price - price * 10 / 100, 2), prices))

    # Keep only the discounted prices that are above 300 using filter()
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))

    return discounted_prices, filtered_prices


# Testing
discounted_prices, filtered_prices = process_prices([100, 500, 900, 50, 750])

print("Discounted prices:", discounted_prices)
print("Filtered prices (above 300):", filtered_prices)
