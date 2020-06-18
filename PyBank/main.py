
import os

import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

print("opening", csvpath)

count_of_months = 0
with open(csvpath) as csvfile:
    print(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("Financial Analysis ", type(csv_header)) 
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        count_of_months += 1
count_of_months