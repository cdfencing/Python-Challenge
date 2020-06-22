import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print("opening", csvpath)
count_of_month = 1

x = 0
y = 0

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first 
    csv_header = next(csvreader) 
    csv_init = next(csvreader) #grabbing starting values under header

    startdate = csv_init[0]
    initPL = csv_init[1]

    total = int(initPL)


    print("Financial Analysis: ") 
    print("------------------------")

    
    monthly_changes = []
    
    for row in csvreader: #now starting at row 3 in data
        #grab value from the next row, 
        total = total + int(row[1]) 
        count_of_month += 1 

        if count_of_month > 0: # do this every time, starting with the second time
            monthly_change = int(row[1]) - int(initPL)
            monthly_changes.append(monthly_change)
     
        max_inc_profit = (int(row[1])) - int(initPL)
        
        if max_inc_profit > x: #x stands for current max profit
            x = max_inc_profit
            maxp_date = row[0]
        
        max_dec_profit = (int(row[1])) - int(initPL)
        
        if max_dec_profit < y: #y stands for current max loss
            y = max_dec_profit 
            maxl_date = row[0]
        
        initPL = int(row[1]) #iterates through the data
    
    Average_Changes = sum(monthly_changes) / len(monthly_changes)
    Average_Changes = round(Average_Changes,2)


    print(f"Total Months: {count_of_month}")  
    print(f"Total: ${total}")
    print(f"Average Change: ${Average_Changes}") 
    print(f"Greatest Increase in Profits: {maxp_date} (${x}) ") 
    print(f"Greatest Decrease in Profits: {maxl_date} (${y}) ")   
   
