# Assignment 3 - Task 3: Lambda Function - GST Calculator

# Price after adding 18% GST
gst = lambda price: price + (0.18 * price)

print(gst(100))   # should print 118.0

# Extra (optional): final price after GST and then a discount
final_price = lambda price, discount_percent: gst(price) - (gst(price) * discount_percent / 100)

print(final_price(100, 10))   # 118 with 10% off = 106.2
