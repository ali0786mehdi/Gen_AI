# Assignment 3 - Task 5: Using filter() - Filter Expensive Products

prices = [100, 250, 400, 1200, 50, 2000, 850]

# Prices greater than 500
expensive = list(filter(lambda price: price > 500, prices))

# Prices less than or equal to 500
affordable = list(filter(lambda price: price <= 500, prices))

print("Prices greater than 500:", expensive)
print("Prices 500 or less:", affordable)
