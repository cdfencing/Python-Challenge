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

Khan_percent = 0
Li_percent = 0
Correy_percent = 0
OTooley_percent = 0

Khan = "Khan"
Li = "Li"
Correy = "Correy"
OTooley = "O'Tooley"

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
    
    Khan_percent = (Khan_votes / total) * 100 
    Khan_percent = round(Khan_percent,3)

    Correy_percent = (Correy_votes / total) * 100 
    Correy_percent = round(Correy_percent,3)

    Li_percent = (Li_votes / total) * 100 
    Li_percent = round(Li_percent,3)

    OTooley_percent = (OTooley_votes / total) * 100 
    OTooley_percent = round(OTooley_percent,3)

    if Khan_percent > Correy_percent and Li_percent and OTooley_percent:
        winner = Khan
    elif Correy_percent > Khan_percent and Li_percent and OTooley_percent:
        winner = Correy
    elif Li_percent > Khan_percent and Correy_percent and OTooley_percent:
        winner = Li
    elif OTooley_percent > Khan_percent and Correy_percent and Li_percent:
        winner = OTooley

    print("Election Results: ") 
    print("------------------------")
    print(f"Total Votes: {total}")
    print("------------------------")
    print(f"Khan: {Khan_percent}% ({Khan_votes}) ")
    print(f"Correy: {Correy_percent}% ({Correy_votes}) ")
    print(f"Li: {Li_percent}% ({Li_votes}) ")
    print(f"O'Tooley: {OTooley_percent}% ({OTooley_votes}) ")
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")

with open(output_path, "Analysis") as textfile:
    textfile.write(report)