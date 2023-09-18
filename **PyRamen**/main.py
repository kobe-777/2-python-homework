from pathlib import Path
import csv

# Initialize empty lists to hold menu and sales data
menu = []
sales = []

# Read in menu_data.csv
with open('Resources/menu_data.csv', 'r', newline='') as menu_file:
    menu_reader = csv.reader(menu_file)
    next(menu_reader)  # Skip the header row
    for row in menu_reader:
        menu.append(row)

# Read in sales_data.csv
with open('Resources/sales_data.csv', 'r', newline='') as sales_file:
    sales_reader = csv.reader(sales_file)
    next(sales_reader)  # Skip the header row
    for row in sales_reader:
        sales.append(row)

# Initialize an empty report dictionary to hold future aggregated per-product results
report = {
}

# Loop through every row in the 'sales' list object
for sale in sales:
    # Extract quantity and sales item
    quantity = int(sale[3])
    sales_item = sale[4]
    
    # Perform check if 'sales_item' is included in the 'report'. If not, initiliaze the key-value pairs
    if sales_item not in report:
        report[sales_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }
    
    # Create a nested loop through every row in 'menu', set the metrics
    for menu_item in menu:
        item = menu_item[0]
        price = float(menu_item[3])
        cost = float(menu_item[4])
        
        # If there's a match, calculate and update metrics in 'report', else print the message
        if sales_item == item:
            profit = price - cost
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        else:
            print(f"{sales_item} does not equal {item}! NO MATCH!")

# Write the contents of 'report' to a text file
with open('report.txt', 'w') as report_file:
    for item, metrics in report.items():
        report_file.write(f"{item} {metrics}\n")