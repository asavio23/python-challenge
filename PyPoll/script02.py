import os 
import csv 

myfile = os.path.join('Resources','election_data.csv')

#Track Total Votes
total_votes = 0

#Candidate list/Indivdual Votes
candidate_lists = []
candidate_votes = {}

#Winning Canidate & Tracker 
winning_candidate = ""
winning_votes = 0 

#Read CSV
with open (myfile) as csv_file:
    csvreader = csv.reader(csv_file, delimiter =",")
    csv_header = next(csvreader)

 for row in csvreader:

    #tally votes and candidate name
    total_votes = total_votes + 1 
    candidate_name = row[2] 

    #if the name doesnt exist in list.. Add and track their votes
    if candidate_name not in candidate_lists:
        candidate_lists.append(candidate_name)
        candidate_votes[candidate_name] = 0 
    candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 

#print 
print_results = str(
    f"\n\n Election Results\n"
    f"----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n"
)
print(print_results)

output = os.path.join ('Analysis', 'budget_summary.txt')
file = open(output, "w")
file.write(print_statement)





