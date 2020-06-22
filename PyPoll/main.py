import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
print("opening", csvpath) 

total = 0
candidates_list = []

Khan_votes =0
Li_votes = 0
Correy_votes = 0
OTooley_votes = 0

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # Read the header row first
    
    for row in csvreader: #now starting at row 2
        total += 1
        
        candidate = row[2]

        if candidate == "Khan": 
            Khan_votes += 1
        if candidate == "Li":
            Li_votes += 1
        if candidate == "Correy":
            Correy_votes += 1
        if candidate == "O'Tooley":
            OTooley_votes += 1

    print("Election Results: ") 
    print("------------------------")


    print(f"Total Votes: {total}")
    print("------------------------")
    