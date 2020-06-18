
import os

import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

print("opening", csvpath)

count_of_month = 0


with open(csvpath) as csvfile:
    print(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("Financial Analysis ") 
    print("_________________________")

    for row in csvreader:
        count_of_month += 1
    print(f"Total Months: {count_of_month}")

    total = 0
    for row in csvreader:
        total += int(row[1])
    print(f"Total: ${total}")
    #DEBUG! NEED TO FIGURE OUT HOW TO TOTAL THE COLUMN

    #for row in csvreader:
        #count_of_month += 1
    #print(f"Average  Change: {count_of_month}")

    #for row in csvreader:
        #count_of_month += 1
    #print(f"Greatest Increase in Profits: {count_of_month}")

    #for row in csvreader:
        #count_of_month += 1
    #print(f"Greatest Decrease in Profits: {count_of_month}")



