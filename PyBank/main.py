
import os

import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

print("opening", csvpath)

count_of_month = 0
total = 0

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None) #skip header
   
    total = total + csvreader[1]
    print(csvfile)
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("Financial Analysis ") 
    print("_________________________")

    for roiw in csvreader:
        count_of_month += 1
    print(f"Total Months: {count_of_month}")

    for i in csvreader:
        total += int(i[1])
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



