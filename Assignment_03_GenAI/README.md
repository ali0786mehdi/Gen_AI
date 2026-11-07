# Python Functions - Billing and Utility Automation

A set of small Python programs for an online billing system. They demonstrate
user-defined functions, recursion, lambda functions, `map()`, `filter()` and
default arguments.

No external libraries are needed. Only built-in Python is used.

## Requirements
- Python 3.6 or newer

Check your version:
```
python --version
```
(On some systems use `python3` instead of `python`.)

## Project Structure
```
assignment3/
├── task1.py    # Function with a default argument (discount)
├── task2.py    # Recursive factorial
├── task3.py    # Lambda GST calculator
├── task4.py    # map() to apply GST to a list
├── task5.py    # filter() to split expensive and affordable prices
├── task6.py    # Combined function using map() and filter()
├── task7.py    # Interactive menu using functions
└── README.md
```

## How to Run
1. Download or clone the project folder.
2. Open a terminal (Command Prompt, PowerShell or Terminal).
3. Go to the project folder:
   ```
   cd assignment3
   ```
4. Run any program:
   ```
   python task1.py
   python task2.py
   python task3.py
   python task4.py
   python task5.py
   python task6.py
   python task7.py
   ```
Tasks 1 to 6 print their results straight away. Task 7 is interactive and
waits for your input.

---

## Programs

### task1.py - Price After Discount
`apply_discount(price, discount_percent=5)` returns the price after discount.
If the discount is not given, 5% is used. A discount above 60% is limited to 60%.

Output:
```
900.0
475.0
400.0
```
The three lines are `apply_discount(1000, 10)`, `apply_discount(500)` and
`apply_discount(1000, 80)`. The last one is capped at 60%.

### task2.py - Factorial (Recursive)
`factorial(n)` calls itself until it reaches 0 or 1. For a negative number it
prints an error message instead of a result.

Output:
```
factorial(5): 120
factorial(0): 1
factorial(-3):
Error: factorial is not defined for negative numbers.
```

### task3.py - GST Calculator (Lambda)
`gst` is a lambda that adds 18% GST to a price. An extra lambda,
`final_price`, applies GST and then a discount.

Output:
```
118.0
106.2
```

### task4.py - map()
Applies the `gst` lambda to every price in the list using `map()`.

Output:
```
Original prices: [100, 250, 400, 1200, 50]
Prices after GST: [118.0, 295.0, 472.0, 1416.0, 59.0]
```

### task5.py - filter()
Splits a list of prices into those above 500 and those 500 or below.

Output:
```
Prices greater than 500: [1200, 2000, 850]
Prices 500 or less: [100, 250, 400, 50]
```

### task6.py - Combined Utility Function
`process_prices(prices)` takes a list, applies a 10% discount to every price
with `map()`, then keeps only the discounted prices above 300 with `filter()`.
It returns both lists.

Output for `[100, 500, 900, 50, 750]`:
```
Discounted prices: [90.0, 450.0, 810.0, 45.0, 675.0]
Filtered prices (above 300): [450.0, 810.0, 675.0]
```

### task7.py - Price Menu
An interactive menu built on three small functions: `add_price`,
`get_average_price` and `get_max_price`.

| Option | Action |
|--------|--------|
| `1` | Add a price (whole or decimal number) |
| `2` | Show the average price |
| `3` | Show the highest price |
| `q` | Quit |

Invalid choices or non-numeric prices show a message and the menu appears
again. Asking for the average or highest price before adding any prices shows
"No prices added yet." Prices are kept only while the program is running.

Example session:
```
Choose an option: 1
Enter a price: 100
Price added.
Choose an option: 1
Enter a price: 250.5
Price added.
Choose an option: 2
Average price: 175.25
Choose an option: 3
Highest price: 250.5
Choose an option: q
Goodbye!
```

## Notes
- To try other values, edit the lists (`prices`) at the top of Tasks 4, 5 and 6.
- The programs do not use classes, packages, exceptions or file handling.

## Troubleshooting
| Problem | Fix |
|---------|-----|
| `python` is not recognized | Install Python from python.org, or try `python3` |
| `No such file or directory` | Make sure you are inside the `assignment3` folder |
| Program closes immediately on double-click | Run it from a terminal instead |
