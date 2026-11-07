# Assignment 3 - Task 1: Basic Function - Price After Discount

def apply_discount(price, discount_percent=5):
    # Extra (optional): discount can never be more than 60%
    if discount_percent > 60:
        discount_percent = 60

    discount_amount = price * discount_percent / 100
    return price - discount_amount


# Testing
print(apply_discount(1000, 10))   # 10% discount given
print(apply_discount(500))        # uses the default 5% discount
print(apply_discount(1000, 80))   # 80% is too high, so 60% is applied
