import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
print("opening", csvpath)
count_of_votes = 1



with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) # Read the header row first
    csv_init = next(csvreader) #grabbing starting values under header

    candidate_votes = csv_init[0]
    candidate = csv_init[1] #need to make this a list so it pulls both names

    total = int(candidate_votes)

    print(candidate)
    print(candidate_votes)

    print("Election Results: ") 
    print("------------------------")

    for row in csvreader: #now starting at row 3 in data
        #grab value from the next row, 
        total = total + int(row[0])
        count_of_votes += 1




    print(f"Total Votes: {count_of_votes}")
    print("------------------------")