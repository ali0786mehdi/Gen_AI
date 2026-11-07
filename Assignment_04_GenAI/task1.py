# Assignment 4 - Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

# Open the file in write mode and write each sale on a new line
with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

# The with block closes the file automatically.
# Now reopen it in read mode and print the contents.
with open("sales_data.txt", "r") as file:
    content = file.read()

print("Contents of sales_data.txt:")
print(content)

# Extra (optional): write the same data in comma-separated format
# (saved in a separate file so the other tasks are not affected)
with open("sales_data_csv.txt", "w") as file:
    comma_text = ""
    for sale in sales:
        comma_text = comma_text + str(sale) + ","
    comma_text = comma_text[:-1]      # remove the last comma
    file.write(comma_text)

with open("sales_data_csv.txt", "r") as file:
    print("Comma-separated version:")
    print(file.read())
