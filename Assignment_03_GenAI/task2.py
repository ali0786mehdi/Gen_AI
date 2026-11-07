# Assignment 3 - Task 2: Recursive Function - Factorial Utility

def factorial(n):
    # Negative numbers have no factorial
    if n < 0:
        print("Error: factorial is not defined for negative numbers.")
        return None

    # Base cases: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


# Testing
print("factorial(5):", factorial(5))
print("factorial(0):", factorial(0))
print("factorial(-3):")
factorial(-3)
