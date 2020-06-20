
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print("opening", csvpath)
count_of_month = 1

avg = 0
x = 0



with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    csv_init = next(csvreader) #grabbing starting values under header

    startdate = csv_init[0]
    initPL = csv_init[1]

    total = int(initPL)

    print(startdate)
    print(initPL)

    print("Financial Analysis: ") 
    print("------------------------")
    
    for row in csvreader: #now starting at row 3 in data
        #grab value from the next row, 
        total = total + int(row[1]) #debug
        count_of_month += 1 #debug
         
        max_inc_profit = (int(row[1])) - int(initPL)
        
        if max_inc_profit > x: #x stands for current max profit
            x = max_inc_profit
            maxp_date = row[0]
        
        initPL = int(row[1])
    #     #avg = total / len(row[1]) #debug, not right value
        
    #     #max_dec_profit = min(row[1]) #debug, not right value need if statement
    
    print(f"Total Months: {count_of_month}")  
    print(f"Total: ${total}")
    #print(f"Average Change: {avg}") #debug
    print(f"Greatest Increase in Profits: {maxp_date} {max_inc_profit}") #debug
    # #print(f"Greatest Decrease in Profits: {max_dec_profit}") #debug      
    
    
    
    
    # #headerrow = next(csvreader) #skip header
    # #nextrow = next(csvreader) # grab next row 
   
    

    # #for row in csvreader:
    #     #count_of_month += 1
    

    # #for row in csvreader:
    #     #count_of_month += 1
    

    # #for row in csvreader:
    #     #count_of_month += 1
    



