# Python File Handling - Retail Sales Utilities

A set of small Python programs for a retail analytics team. They show how to
open files in different modes, read and write text files, append records,
extract data and generate reports.

No external libraries are needed. Only built-in Python is used (`os` is part of
the standard library and is used only to check if a file exists).

## Requirements
- Python 3.6 or newer

Check your version:
```
python --version
```
(On some systems use `python3` instead of `python`.)

## Project Structure
```
assignment4/
├── task1.py    # Write sales records to a file
├── task2.py    # Read the file with read(), readline(), readlines()
├── task3.py    # Append new sales
├── task4.py    # Summary report from the file
├── task5.py    # Create a product file from user input
├── task6.py    # Read a file safely using os.path.exists()
├── task7.py    # Export discounted prices to a report
└── README.md
```

## How to Run
1. Download or clone the project folder.
2. Open a terminal (Command Prompt, PowerShell or Terminal).
3. Go to the project folder:
   ```
   cd assignment4
   ```
4. Run the tasks **in order**:
   ```
   python task1.py
   python task2.py
   python task3.py
   python task4.py
   python task5.py
   python task6.py
   python task7.py
   ```

### Important
- Always run the commands from **inside** the project folder, because the
  programs create and read files in the current folder.
- Task 1 creates `sales_data.txt`. Tasks 2, 3 and 4 depend on it, so run
  Task 1 first.
- Task 3 appends to the file. If you run it more than once, the values are added
  again. To reset, run `task1.py` again (it overwrites the file).
- Task 4 gives the numbers shown below only after Task 1 and Task 3 have each
  been run once.

## Files Created by the Programs
| File | Created by |
|------|-----------|
| `sales_data.txt` | task1.py (updated by task3.py) |
| `sales_data_csv.txt` | task1.py (optional comma-separated version) |
| `products.txt` | task5.py |
| `discount_report.txt` | task7.py |

---

## Programs

### task1.py - Write Sales Records
Writes the sales `[1200, 450, 980, 1500, 3000]` to `sales_data.txt`, one per line,
then reopens the file and prints it. It also saves a comma-separated version
in `sales_data_csv.txt`.

Output:
```
Contents of sales_data.txt:
1200
450
980
1500
3000

Comma-separated version:
1200,450,980,1500,3000
```

### task2.py - Read in Different Ways
Reads `sales_data.txt` three ways: `read()` for the whole file, `readline()`
for the first line only, and `readlines()` converted into a list of integers.
Newline characters are removed with `strip()`.

Output (last part):
```
Using readline():
1200

Using readlines() converted to integers:
[1200, 450, 980, 1500, 3000]
```

### task3.py - Append New Sales
Appends `5000, 2500, 1700` to `sales_data.txt`, then prints the whole file and
the total number of lines.

Output (last part):
```
5000
2500
1700

Total number of lines: 8
```

### task4.py - Summary Report
Reads all values from `sales_data.txt`, converts them to integers and prints
the summary.

Output:
```
===== Sales Summary Report =====
Total Sales: 16330
Highest Sale: 5000
Lowest Sale: 450
Average Sale: 2041.25
```

### task5.py - Product Info File
Asks for 3 product names and prices, saves them to `products.txt` in the format
`ProductName | Price`, then reads the file back and prints it. If a price is
not a number, it asks again.

Example:
```
Enter name of product 1: Pen
Enter price of Pen: 10
Enter name of product 2: Book
Enter price of Book: 250.5
Enter name of product 3: Bag
Enter price of Bag: 999

Contents of products.txt:
Pen | 10
Book | 250.5
Bag | 999
```

### task6.py - Read a File Safely
Asks for a filename. If the file exists, its contents are printed. If not, the
program prints a message instead of crashing.

Existing file:
```
Enter the filename to open: products.txt

Contents of products.txt:
Pen | 10
Book | 250.5
Bag | 999
```
Missing file:
```
Enter the filename to open: nothing.txt
File not found. Please check the filename.
```

### task7.py - Export Discounted Prices
Asks for a discount percentage (0 to 100), applies it to the products in the
dictionary, writes the result to `discount_report.txt`, then reads the file
and prints it. A summary with the number of items and the average discounted
price is added at the bottom.

Example with a 10% discount:
```
Enter discount percentage: 10

Contents of discount_report.txt:
Product | Original Price | Discounted Price
Mouse | 500 | 450.0
Keyboard | 800 | 720.0
Monitor | 7000 | 6300.0
Pendrive | 400 | 360.0
Camera | 5000 | 4500.0

Total Items: 5
Average Discounted Price: 2466.0
```

## Notes
- All files are opened with `with open(...)`, so they are closed automatically.
- Running a program again overwrites its output file, except `task3.py`,
  which appends to `sales_data.txt`.
- The programs do not use pandas, the csv module or any external tools.

## Troubleshooting
| Problem | Fix |
|---------|-----|
| `python` is not recognized | Install Python from python.org, or try `python3` |
| `FileNotFoundError: sales_data.txt` | Run `task1.py` first, from inside the `assignment4` folder |
| Task 4 shows different totals | `sales_data.txt` was changed. Run `task1.py`, then `task3.py` once |
| Program closes immediately on double-click | Run it from a terminal instead |
