from pathlib import Path
import csv

# Set the file path
csvpath = Path("Resources/budget_data.csv")

# Initialize variables to hold metrics
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
average_change = 0
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read the file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Go to the next row from the start of the file
    header = next(csvreader)
    
    # Loop through the rows in the CSV file
    for row in csvreader:
        
        # Extract date and profit/loss
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total months and total profit/loss
        total_months += 1
        total_profit_loss += profit_loss
        
        # Calculate the change in profit/loss
        change = profit_loss - previous_profit_loss
        
        # Update the greatest increase and decrease
        if change > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change
        elif change < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = round(total_profit_loss / (total_months - 1), 2)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_loss}\n")
    textfile.write(f"Average  Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")