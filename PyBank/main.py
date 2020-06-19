
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print("opening", csvpath)
count_of_month = 0
total = 0
avg = 0
max_inc_profit = 0
max_dec_profit = 0

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("Financial Analysis: ") 
    print("------------------------")
    for row in csvreader:
        #grab value from the next row, 
        # it is now in a list (grabs second value)
        total = total + int(row[1])
        count_of_month += 1
        avg = total / len(row[1]) #debug, not right value
        max_inc_profit = max(row[1]) #debug, not right value
        max_inc_profit = min(row[1]) #debug, not right value
    
    print(f"Total Months: {count_of_month}")  
    print(f"Total: ${total}")
    print(f"Average Change: {avg}") #debug
    print(f"Greatest Increase in Profits: {max_inc_profit}") #debug
    print(f"Greatest Decrease in Profits: {max_dec_profit}") #debug      
    
    
    
    
    #headerrow = next(csvreader) #skip header
    #nextrow = next(csvreader) # grab next row 
   
    

    #for row in csvreader:
        #count_of_month += 1
    

    #for row in csvreader:
        #count_of_month += 1
    

    #for row in csvreader:
        #count_of_month += 1
    



