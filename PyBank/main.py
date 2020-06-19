
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print("opening", csvpath)
count_of_month = 0
total = 0

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
            
    headerrow = next(csvreader) #skip header
    nextrow = next(csvreader) # grab next row
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("Financial Analysis: ") 
    print("_ _ _ _ _ _ _ _ _ _ _ _ _")
    for row in csvreader:
        count_of_month += 1
    print(f"Total Months: {count_of_month}")
    
    #grab value from the next row, it is now in a list (grabs second value)
    total = total + int(nextrow[1])
    print(f"Total: ${total}")

    
    #print(f"Total Months: {count_of_month}")
    #for i in csvreader:
        #total += int(i[1])
    #print(f"Total: ${total}")
   
   
    

    #for row in csvreader:
        #count_of_month += 1
    #print(f"Average  Change: {count_of_month}")

    #for row in csvreader:
        #count_of_month += 1
    #print(f"Greatest Increase in Profits: {count_of_month}")

    #for row in csvreader:
        #count_of_month += 1
    #print(f"Greatest Decrease in Profits: {count_of_month}")



