# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = [0]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total = int(first_row[1])
    change = int(first_row[1])
    for row in reader:

        # Track the total
        
        total += int(row[1])
        change = int(row[1])-change 
        # Track the net change
        net_change_list.append(change)
        month_of_change.append(row[0])

dictionary = dict(zip(month_of_change, net_change_list))
        # Calculate the greatest increase
greatest_increase =  max(dictionary.items(), key=lambda k: k[1])
            
        # Calculate the greatest decrease
greatest_decrease =  min(dictionary.items(), key=lambda k: k[1])
            
# Calculate the Average Net Change

total_months = len(month_of_change) + 1
    
net_monthly_avg = sum(net_change_list)/total_months
# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
file = open("output.txt","w")
file.write(output)
file.close()