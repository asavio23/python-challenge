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
print_results = (
    f"\n\n Election Results\n"
    f"----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n"
)
print(print_results)

voter_output = ""
#retreieve the counts & precentages
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percent = float(votes) / float(total_votes) * 100 

#determine winners with respect to their vote tally
    if (votes > winning_votes): 
        winning_votes = votes 
        winning_candidate = candidate
    voter_output += f"{candidate}: {vote_percent:.2f}% ({votes})\n"
print(voter_output)

winning_summary = (
    f"-------------------\n"
    f"Winner: {winning_candidate} "
)
print(winning_summary)

    #add to analysis
output = os.path.join ('Analysis', 'election_summary.txt')
file = open(output, "w")
file.write(print_results)
file.write(voter_output)
file.write(winning_summary)





